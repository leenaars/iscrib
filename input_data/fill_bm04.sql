# Original bm04 gave by Anne Laure Pantin we keep it for comparation purpose
#

#
# Structure de la table `bm04`
#
DROP TABLE IF EXISTS `bm04`;
CREATE TABLE `bm04` (
  `Code_bib` int default NULL,
  `exer` int default NULL,
  `A11` int default NULL,
  `A12` int default NULL,
  `A13` int default NULL,
  `A14` int default NULL,
  `A15` int default NULL,
  `A16` int default NULL,
  `A21` int default NULL,
  `A22` int default NULL,
  `A23` int default NULL,
  `A24` int default NULL,
  `A31` int default NULL,
  `A32` int default NULL,
  `A33` int default NULL,
  `B11X` int default NULL,
  `B11Y` int default NULL,
  `B11Z` int default NULL,
  `B12X` int default NULL,
  `B12Y` int default NULL,
  `B12Z` int default NULL,
  `B13X` int default NULL,
  `B13Y` int default NULL,
  `B13Z` int default NULL,
  `B21` int default NULL,
  `B22` int default NULL,
  `B23` int default NULL,
  `B31` char(1) default NULL,
  `B32` varchar(40) default NULL,
  `B33` char(1) default NULL,
  `B34` char(1) default NULL,
  `B35` varchar(60) default NULL,
  `B36` char(1) default NULL,
  `B37` int default NULL,
  `B38X` int default NULL,
  `B38Y` int default NULL,
  `B39X` int default NULL,
  `B39Y` int default NULL,
  `B40X` char(1) default NULL,
  `B40Y` char(1) default NULL,
  `B41` char(1) default NULL,
  `B42` char(1) default NULL,
  `B43` char(1) default NULL,
  `C11W` int default NULL,
  `C11X` int default NULL,
  `C11Y` int default NULL,
  `C11Z` int default NULL,
  `C12W` int default NULL,
  `C12X` int default NULL,
  `C12Y` int default NULL,
  `C12Z` int default NULL,
  `C13W` int default NULL,
  `C13X` int default NULL,
  `C13Y` int default NULL,
  `C13Z` int default NULL,
  `C14W` int default NULL,
  `C14X` int default NULL,
  `C14Y` int default NULL,
  `C14Z` int default NULL,
  `C15W` int default NULL,
  `C15X` int default NULL,
  `C15Y` int default NULL,
  `C15Z` int default NULL,
  `C16W` int default NULL,
  `C16X` int default NULL,
  `C16Y` int default NULL,
  `C16Z` int default NULL,
  `C17W` int default NULL,
  `C17X` int default NULL,
  `C17Y` int default NULL,
  `C17Z` int default NULL,
  `C21W` int default NULL,
  `C21X` int default NULL,
  `C21Y` int default NULL,
  `C21Z` int default NULL,
  `C22W` int default NULL,
  `C22X` int default NULL,
  `C22Y` int default NULL,
  `C22Z` int default NULL,
  `C23W` int default NULL,
  `C23X` int default NULL,
  `C23Y` int default NULL,
  `C23Z` int default NULL,
  `C31W` int default NULL,
  `C31X` int default NULL,
  `C31Y` int default NULL,
  `C31Z` int default NULL,
  `C32W` int default NULL,
  `C32X` int default NULL,
  `C33W` int default NULL,
  `C33X` int default NULL,
  `C33Y` int default NULL,
  `C33Z` int default NULL,
  `C34W` int default NULL,
  `C34X` int default NULL,
  `C41W` int default NULL,
  `C41Y` int default NULL,
  `C41Z` int default NULL,
  `C42W` int default NULL,
  `C42Y` int default NULL,
  `C42Z` int default NULL,
  `C43W` int default NULL,
  `C43X` int default NULL,
  `C43Y` int default NULL,
  `C51` int default NULL,
  `D11X` int default NULL,
  `D11Y` int default NULL,
  `D11Z` int default NULL,
  `D12X` int default NULL,
  `D12Y` int default NULL,
  `D12Z` int default NULL,
  `D13X` int default NULL,
  `D13Y` int default NULL,
  `D13Z` int default NULL,
  `D14X` int default NULL,
  `D14Y` int default NULL,
  `D14Z` int default NULL,
  `D15X` int default NULL,
  `D15Y` int default NULL,
  `D15Z` int default NULL,
  `D16X` int default NULL,
  `D16Y` int default NULL,
  `D16Z` int default NULL,
  `D17X` int default NULL,
  `D17Y` int default NULL,
  `D17Z` int default NULL,
  `D18X` int default NULL,
  `D18Y` int default NULL,
  `D18Z` int default NULL,
  `D19Z` int default NULL,
  `D20Z` int default NULL,
  `D21Z` int default NULL,
  `D22Z` int default NULL,
  `D23Z` int default NULL,
  `D24Z` int default NULL,
  `D25Z` int default NULL,
  `D31` int default NULL,
  `D32` int default NULL,
  `D33` int default NULL,
  `D34` int default NULL,
  `D41` int default NULL,
  `D42` int default NULL,
  `D43` int default NULL,
  `D44` int default NULL,
  `D45` int default NULL,
  `D46` int default NULL,
  `D47` int default NULL,
  `D48` int default NULL,
  `E11X` int default NULL,
  `E11Y` int default NULL,
  `E11Z` int default NULL,
  `E12X` int default NULL,
  `E12Y` int default NULL,
  `E12Z` int default NULL,
  `E13X` int default NULL,
  `E13Y` int default NULL,
  `E13Z` int default NULL,
  `E14X` int default NULL,
  `E14Y` int default NULL,
  `E14Z` int default NULL,
  `E15X` int default NULL,
  `E15Y` int default NULL,
  `E15Z` int default NULL,
  `E21X` int default NULL,
  `E21Y` int default NULL,
  `E21Z` int default NULL,
  `E22X` int default NULL,
  `E22Y` int default NULL,
  `E22Z` int default NULL,
  `E23X` int default NULL,
  `E23Y` int default NULL,
  `E23Z` int default NULL,
  `E24X` int default NULL,
  `E24Y` int default NULL,
  `E24Z` int default NULL,
  `E25X` int default NULL,
  `E25Y` int default NULL,
  `E25Z` int default NULL,
  `E26X` int default NULL,
  `E26Y` int default NULL,
  `E26Z` int default NULL,
  `E27X` int default NULL,
  `E27Y` int default NULL,
  `E27Z` int default NULL,
  `E31X` int default NULL,
  `E31Y` int default NULL,
  `E31Z` int default NULL,
  `E32X` int default NULL,
  `E32Y` int default NULL,
  `E32Z` int default NULL,
  `E33X` int default NULL,
  `E33Y` int default NULL,
  `E33Z` int default NULL,
  `E34X` int default NULL,
  `E34Y` int default NULL,
  `E34Z` int default NULL,
  `E35X` int default NULL,
  `E35Y` int default NULL,
  `E35Z` int default NULL,
  `E36X` int default NULL,
  `E36Y` int default NULL,
  `E36Z` int default NULL,
  `E37X` int default NULL,
  `E37Y` int default NULL,
  `E37Z` int default NULL,
  `E38X` int default NULL,
  `E38Y` int default NULL,
  `E38Z` int default NULL,
  `E41X` int default NULL,
  `E41Y` int default NULL,
  `E41Z` int default NULL,
  `E42X` int default NULL,
  `E42Y` int default NULL,
  `E42Z` int default NULL,
  `E43X` int default NULL,
  `E43Y` int default NULL,
  `E43Z` int default NULL,
  `E44X` int default NULL,
  `E44Y` int default NULL,
  `E44Z` int default NULL,
  `E51X` int default NULL,
  `E51Y` int default NULL,
  `E51Z` int default NULL,
  `E52X` int default NULL,
  `E52Y` int default NULL,
  `E52Z` int default NULL,
  `E61X` int default NULL,
  `E61Y` int default NULL,
  `E61Z` int default NULL,
  `E62X` int default NULL,
  `E62Y` int default NULL,
  `E62Z` int default NULL,
  `E63X` int default NULL,
  `E63Y` int default NULL,
  `E63Z` int default NULL,
  `E64X` int default NULL,
  `E64Y` int default NULL,
  `E64Z` int default NULL,
  `E65X` int default NULL,
  `E65Y` int default NULL,
  `E65Z` int default NULL,
  `E66X` int default NULL,
  `E66Y` int default NULL,
  `E66Z` int default NULL,
  `E67X` int default NULL,
  `E67Y` int default NULL,
  `E67Z` int default NULL,
  `E68Z` int default NULL,
  `E69X` int default NULL,
  `E69Y` int default NULL,
  `E69Z` int default NULL,
  `E70X` int default NULL,
  `E70Y` int default NULL,
  `E70Z` int default NULL,
  `E71X` int default NULL,
  `E71Y` int default NULL,
  `E71Z` int default NULL,
  `E72X` int default NULL,
  `E72Y` int default NULL,
  `E72Z` int default NULL,
  `F11` char(1) default NULL,
  `F12` char(1) default NULL,
  `F13` varchar(60) default NULL,
  `F14` char(1) default NULL,
  `F15` varchar(60) default NULL,
  `F16` char(1) default NULL,
  `F17` char(1) default NULL,
  `F18` char(1) default NULL,
  `F19` char(1) default NULL,
  `F20` char(1) default NULL,
  `G11Lu` char(1) default NULL,
  `G11Ma` char(1) default NULL,
  `G11Me` char(1) default NULL,
  `G11je` char(1) default NULL,
  `G11ve` char(1) default NULL,
  `G11Sa` char(1) default NULL,
  `G11Di` char(1) default NULL,
  `G12` varchar(10) default NULL,
  `G13` varchar(10) default NULL,
  `G21W` int default NULL,
  `G21X` int default NULL,
  `G21Y` int default NULL,
  `G21Z` int default NULL,
  `G22W` int default NULL,
  `G22X` int default NULL,
  `G22Y` int default NULL,
  `G23W` int default NULL,
  `G23X` int default NULL,
  `G23Y` int default NULL,
  `G24W` int default NULL,
  `G24X` int default NULL,
  `G24Y` int default NULL,
  `G25W` int default NULL,
  `G25X` int default NULL,
  `G25Y` int default NULL,
  `G25Z` int default NULL,
  `G26Y` int default NULL,
  `G26Z` int default NULL,
  `G27Y` int default NULL,
  `G27Z` int default NULL,
  `G28` int default NULL,
  `G29` int default NULL,
  `G30` int default NULL,
  `G31` int default NULL,
  `G41X` int default NULL,
  `G41Y` int default NULL,
  `G41Z` int default NULL,
  `G42X` int default NULL,
  `G42Y` int default NULL,
  `G42Z` int default NULL,
  `G43X` int default NULL,
  `G43Y` int default NULL,
  `G43Z` int default NULL,
  `G44X` int default NULL,
  `G44Y` int default NULL,
  `G44Z` int default NULL,
  `G45X` int default NULL,
  `G45Y` int default NULL,
  `G45Z` int default NULL,
  `G46Z` int default NULL,
  `G47Z` int default NULL,
  `G48X` int default NULL,
  `G48Y` int default NULL,
  `G48Z` int default NULL,
  `G49Z` int default NULL,
  `G50Z` int default NULL,
  `G51Z` int default NULL,
  `H11` char(1) default NULL,
  `H12` char(1) default NULL,
  `H13` char(1) default NULL,
  `H14` char(1) default NULL,
  `H15` char(1) default NULL,
  `H16` int default NULL,
  `H17` int default NULL,
  `H18` varchar(60) default NULL,
  `H21` char(1) default NULL,
  `H22` char(1) default NULL,
  `H23` char(1) default NULL,
  `H24` char(1) default NULL,
  `H25` char(1) default NULL,
  `H26` char(1) default NULL,
  `H27` char(1) default NULL,
  `H29X` int default NULL,
  `H29Y` int default NULL,
  `H29Z` int default NULL,
  `H31` char(1) default NULL,
  `H32Y` int default NULL,
  `H32Z` int default NULL,
  `H33Y` int default NULL,
  `H33Z` int default NULL,
  `H34Y` int default NULL,
  `H34Z` int default NULL,
  `H35Y` int default NULL,
  `H35Z` int default NULL,
  `H36Y` int default NULL,
  `H36Z` int default NULL,
  `H37Y` int default NULL,
  `H37Z` int default NULL,
  `H38Y` int default NULL,
  `H38Z` int default NULL,
  `H39Y` int default NULL,
  `H39Z` int default NULL,
  `H40Y` int default NULL,
  `H40Z` int default NULL,
  `H41Y` int default NULL,
  `H41Z` int default NULL,
  `H42Y` int default NULL,
  `H42Z` int default NULL,
  `H43Y` int default NULL,
  `H43Z` int default NULL,
  `I11` char(1) default NULL,
  `I12` char(1) default NULL,
  `I13` char(1) default NULL,
  `I14` int default NULL,
  `I15` int default NULL,
  `I16` int default NULL,
  `I17` int default NULL,
  `I18` int default NULL,
  `I19` int default NULL,
  `I20` int default NULL,
  `I21` int default NULL,
  `I31` char(1) default NULL,
  `I32` int default NULL,
  `I33` int default NULL,
  `I34` int default NULL,
  `I35` int default NULL,
  `I36` int default NULL,
  `I41` int default NULL,
  `I42Z` int default NULL,
  `I43Y` int default NULL,
  `I43Z` int default NULL,
  `I44Y` int default NULL,
  `I44Z` int default NULL,
  `I45Y` int default NULL,
  `I45Z` int default NULL,
  `I46Y` int default NULL,
  `I46Z` int default NULL,
  `I47Y` int default NULL,
  `I47Z` int default NULL
) TYPE=MyISAM;
