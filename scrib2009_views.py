# -*- coding: UTF-8 -*-
# Copyright (C) 2009 Sylvain Taverne <sylvain@itaapy.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Import from itools
from itools.core import merge_dicts
from itools.datatypes import Date, Integer, Email, Unicode, Boolean
from itools.gettext import MSG
from itools.uri import get_reference, get_uri_path
from itools.stl import stl
from itools.web import BaseView, STLForm, INFO, ERROR
from itools.xapian import AndQuery, OrQuery, PhraseQuery
from itools.xml import XMLParser

# Import from ikaaro
from ikaaro.forms import XHTMLBody, ReadOnlyWidget, DateWidget, RTEWidget
from ikaaro.forms import TextWidget, AutoForm
from ikaaro.resource_views import LoginView, DBResource_Edit
from ikaaro.views import IconsView
from ikaaro.website_views import ForgottenPasswordForm

# Import from scrib
from datatypes import DateLitterale, Identifiant
from utils import execute


def find_user(username, context):
    root = context.root
    results = root.search(username=username)
    if not len(results):
        results = root.search(email=username)
        if not len(results):
            message = ERROR(u"""L'utilisateur "{username}" n'existe """
                    u"pas.", username=username)
            context.message = message
            return
    return root.get_user(results.get_documents()[0].name)



class Scrib_Admin(IconsView):
    access = 'is_admin'
    title = MSG(u"Administration de Scrib")


    def get_namespace(self, resource, context):
        items = [{'icon': '/ui/icons/48x48/folder.png',
                  'title': u"BM",
                  'description': u"Rechercher une BM",
                  'url': 'bm'}]
        items.append({'icon': '/ui/icons/48x48/folder.png',
                      'title': u"BDP",
                      'description': u"Rechercher une BDP",
                      'url': 'bdp'})
        items.append({'icon': '/ui/icons/48x48/html.png',
                      'title': u"Aide générale",
                      'description': u"Modifier l'aide générale",
                      'url': 'aide/;edit'})
        for page in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
            items.append({'icon': '/ui/icons/48x48/html.png',
                          'title': u"Page %s" % page,
                          'description': (u"Modifier l'aide de la page %s" %
                              page),
                          'url': 'Page%s/;edit' % page})
        for name in ('edit', 'browse_users', 'add_user',
                'edit_virtual_hosts', 'export_sql'):
            view = resource.get_view(name)
            items.append({
                'icon': resource.get_method_icon(view, size='48x48'),
                'title': view.title,
                'description': view.description,
                'url': ';%s' % name})
        return {'title': self.title,
                'batch': None,
                'items': items}



class Scrib_Login(LoginView):
    template = '/ui/scrib2009/Scrib_login.xml'


    def get_namespace(self, resource, context):
        namespace = LoginView.get_namespace(self, resource, context)
        # La page n'apparaît pas forcément sur le site_root
        site_root = context.site_root
        echeance_bm = site_root.get_property('echeance_bm')
        namespace['echeance_bm'] = DateLitterale.encode(echeance_bm)
        echeance_bdp = site_root.get_property('echeance_bdp')
        namespace['echeance_bdp'] = DateLitterale.encode(echeance_bdp)
        context.response.status = 403
        return namespace


    def action(self, resource, context, form):
        username = form['username'].strip()
        password = form['password']
        # Check the user exists
        user = find_user(username, context)
        if user is None:
            return
        # Check the password is right
        if not user.authenticate(password):
            context.message = ERROR(u"Le mot de passe est incorrect.")
            return
        # Set cookie
        user.set_auth_cookie(context, password)
        # Set context
        context.user = user
        # Come back
        referrer = context.request.referrer
        if referrer is None:
            goto = get_reference('./')
        else:
            if user.is_bm() or user.is_bdp():
                goto = get_reference('/users/%s' % user.name)
            else:
                path = get_uri_path(referrer)
                if path.endswith(';login'):
                    goto = get_reference('./')
                else:
                    goto = referrer
        return context.come_back(INFO(u"Welcome!"), goto)



class Scrib_Register(AutoForm):
    access = True
    template = '/ui/scrib2009/Scrib_register.xml'
    title = MSG(u"Crééz votre compte pour l'année 2009")
    schema = {'email': Email(mandatory=True),
              'identifiant': Identifiant(mandatory=True)}
    widgets = [TextWidget('email', title=MSG(u"Adresse mél")),
               TextWidget('identifiant',
                   title=MSG(u"Identifiant "
                       u"(tel que porté dans le courrier postal adressé)"))]
    submit_value = MSG(u"Continuer")


    def is_valid(self, resource, context, form):
        email = form['email']
        identifiant = form['identifiant']

        # Do we already have a user with that email?
        root = context.root
        results = root.search(email=email)
        if len(results):
            context.message = ERROR(u"Ce mél est déjà utilisé : essayez "
                    u"le rappel de mot de passe")
            return False

        # Is the code_ua valid?
        code_ua = int(identifiant[2:])
        form = resource.get_resource('bm/%s' % code_ua, soft=True)
        if form is None:
            context.message = ERROR(u"Cet identifiant est invalide.")
            return False

        # Do we already have a user with that code_ua?
        results = root.search(format='user', code_ua=code_ua)
        if len(results):
            # Same email already tested so it's another one with the code_ua
            context.message = ERROR(u"Cet identifiant est enregistré par un "
                    u"autre utilisateur.")
            return False

        return True


    def action(self, resource, context, form):
        if not self.is_valid(resource, context, form):
            return

        return resource.confirm.GET(resource, context)



class Scrib_ForgottenPassword(ForgottenPasswordForm):

    def action(self, resource, context, form):
        username = form['username'].strip()
        username = username

        # Get the user with the given login name
        user = find_user(username, context)
        if user is None:
            return

        # Send email of confirmation
        email = user.get_property('email')
        user.send_forgotten_password(context, email)

        handler = resource.get_resource('/ui/website/forgotten_password.xml')
        return stl(handler)



class Scrib_Confirm(STLForm):
    access = True
    title = MSG(u"Confirmation de création de compte")
    template = '/ui/scrib2009/Scrib_confirm.xml'
    schema = {'email': Email(mandatory=True),
              'identifiant': Identifiant(mandatory=True),
              'confirm_identifiant': Boolean(mandatory=True),
              'confirm_email': Boolean(mandatory=True)}

    def get_namespace(self, resource, context):
        identifiant = context.get_form_value('identifiant')
        code_ua = int(identifiant[2:])
        form = resource.get_resource('bm/%s' % code_ua)
        return {'email': context.get_form_value('email'),
                'identifiant': identifiant,
                'title': form.get_title()}


    def action(self, resource, context, form):
        if not resource.register.is_valid(resource, context, form):
            return

        # Add the user
        email = form['email']
        user = resource.get_resource('/users').set_user(email, password=None)
        identifiant = form['identifiant']
        code_ua = int(identifiant[2:])
        user.set_property('username', 'BM%s' % code_ua)
        form = resource.get_resource('bm/%s' % code_ua)
        user.set_property('title', form.get_title(), language='fr')
        user.set_property('code_ua', code_ua)
        user.set_property('departement', form.get_property('departement'))
        # Set the role
        resource.set_user_role(user.name, 'members')

        # Send confirmation email
        user.send_confirmation(context, email)

        # Update "mel" field
        form.handler.set_value('A114', email)

        # Bring the user to the login form
        message = (u"<p>Un mél de confirmation vient de vous être envoyé à "
                u"l'adresse <strong>{email}</strong>.</p><p>Suivez ses "
                u"instructions pour activer votre compte.</p>".format(email=email))
        return XMLParser(message.encode('utf-8'))



class Scrib_Edit(DBResource_Edit):
    description = MSG(u"Paramétrer Scrib")
    icon = 'preferences.png'
    schema = merge_dicts(DBResource_Edit.schema,
            annee=Integer(mandatory=True, readonly=True),
            echeance_bm=Date(mandatory=True),
            echeance_bdp=Date(mandatory=True),
            responsable_bm=Unicode(mandatory=True),
            responsable_bdp=Unicode(mandatory=True),
            adresse=XHTMLBody,
            contacts=XHTMLBody)
    widgets = (DBResource_Edit.widgets[:3]
            + [ReadOnlyWidget('annee', readonly=True,
                    title=MSG(u"Année des données collectées")),
                DateWidget('echeance_bm',
                    title=MSG(u"Date d'échéance des BM")),
                DateWidget('echeance_bdp',
                    title=MSG(u"Date d'échéance des BDP")),
                TextWidget('responsable_bm', title=MSG(u"Mél d'envoi "
                    u"des accusés de réception au responsable BM "
                    u"(format « Nom <mél> »)")),
                TextWidget('responsable_bdp', title=MSG(u"Mél d'envoi "
                    u"des accusés de réception au responsable BDP "
                    u"(format « Nom <mél> »)")),
                RTEWidget('adresse',
                      title=MSG("Bandeau : adresse de la direction")),
                RTEWidget('contacts',
                    title=MSG("Bandeau : contacts BM et BDP"))]
             + DBResource_Edit.widgets[3:])


    def action(self, resource, context, form):
        DBResource_Edit.action(self, resource, context, form)
        if not context.edit_conflict:
            resource.set_property('echeance_bm', form['echeance_bm'])
            resource.set_property('echeance_bdp', form['echeance_bdp'])
            resource.set_property('responsable_bm', form['responsable_bm'])
            resource.set_property('responsable_bdp', form['responsable_bdp'])
            resource.set_property('adresse', form['adresse'])
            resource.set_property('contacts', form['contacts'])



class Scrib_ExportSql(STLForm):
    access = 'is_admin'
    template = '/ui/scrib2009/Scrib_export_sql.xml'
    title = MSG(u"Export SQL")
    description = MSG(u"Export global et création des tables.")
    icon = 'excel.png'
    schema = {'confirm': Boolean}


    def get_namespace(self, resource, context):
        return {'year': context.site_root.get_year_suffix()}


    def action_bm(self, resource, context, form):
        year = context.site_root.get_year_suffix()
        schema = resource.bm_class.class_handler.schema
        # Ensure field order consistency
        keys = sorted([key for key in schema.keys() if key[0] != 'B'])
        values = ["  `%s` %s," % (key, schema[key].get_sql_schema())
                for key in keys]
        values = "\n".join(values)
        query = []
        if form['confirm']:
            query.append("drop table if exists `bm%s`;" % year)
        query.extend(["create table `bm%s` (" % year,
            "  `code_ua` int(10) unsigned not null,",
            values,
            "  primary key (`code_ua`)",
            ") default charset=utf8 collate=utf8_swedish_ci;"])
        query = "\n".join(query)
        try:
            execute(query, context)
        except Exception:
            return

        context.message = INFO(u"Table bm{year} créée.", year=year)



    def action_annexes(self, resource, context, form):
        year = context.site_root.get_year_suffix()
        schema = resource.bm_class.class_handler.schema
        # Ensure field order consistency
        keys = sorted([key for key in schema.keys() if key[0] == 'B'])
        values = ["  `%s` %s," % (key, schema[key].get_sql_schema())
                for key in keys]
        values = "\n".join(values)
        query = []
        if form['confirm']:
            query.append("drop table if exists `annexes%s`;" % year)
        query.extend(["create table `annexes%s` (" % year,
            "  `code_ua` int(10) unsigned not null,",
            values[:-1], # remove trailing ","
            ") default charset=utf8 collate=utf8_swedish_ci;"])
        query = "\n".join(query)
        try:
            execute(query, context)
        except Exception:
            return

        context.message = INFO(u"Table annexes{year} créée.", year=year)


    def action_export(self, resource, context, form):
        root = context.root
        query = AndQuery(PhraseQuery('format', resource.bm_class.class_id),
                OrQuery(
                    # Formulaires envoyés mais pas encore exportés
                    PhraseQuery('workflow_state', 'pending'),
                    # Formulaires déjà exportés mais écrase
                    PhraseQuery('workflow_state', 'public')))
        results = root.search(query)
        year = resource.get_year_suffix()
        table_bm = "bm%s" % year
        table_annexes = "annexes%s" % year
        query = []
        done = []
        for brain in results.get_documents(sort_by='name'):
            query.append("delete from `%s` where `code_ua`=%s;" % (table_bm,
                brain.code_ua))
            bm = root.get_resource(brain.abspath)
            query.append(bm.get_export_query(table_bm))
            query.append("delete from `%s` where `code_ua`=%s;" % (
                table_annexes, brain.code_ua))
            pageb = bm.get_pageb()
            for form in pageb.get_resources():
                query.append(form.get_export_query(table_annexes,
                    pages=['B'], exclude=[]))
            done.append(int(bm.name))
            print bm.name
            #1153 "Got a packet bigger than 'max_allowed_packet' bytes"
            if len(done) % 250 == 0:
                try:
                    execute("\n".join(query), context)
                except Exception:
                    return
                query = []


        context.message = INFO(u"Les formulaires terminés ont été exportés : "
                u"codes UA {done}.",
                done=u", ".join([unicode(x) for x in sorted(done)]))



class Scrib_ChangePassword(BaseView):

    def GET(self, resource, context):
        access = 'is_admin'
        users = resource.get_resource('/users')
        for user in users.get_resources():
            user.set_password('a')
        # XXX écrit sur une méthode GET
        context.commit = True
        return context.come_back(MSG(u"Done"), goto='/;browse_content')