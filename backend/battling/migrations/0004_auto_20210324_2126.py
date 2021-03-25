# Generated by Django 3.1.7 on 2021-03-24 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battling', '0003_auto_20210322_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='battle',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='battle',
            name='pk32',
            field=models.CharField(choices=[('bulbasaur', 'bulbasaur'), ('ivysaur', 'ivysaur'), ('venusaur', 'venusaur'), ('charmander', 'charmander'), ('charmeleon', 'charmeleon'), ('charizard', 'charizard'), ('squirtle', 'squirtle'), ('wartortle', 'wartortle'), ('blastoise', 'blastoise'), ('caterpie', 'caterpie'), ('metapod', 'metapod'), ('butterfree', 'butterfree'), ('weedle', 'weedle'), ('kakuna', 'kakuna'), ('beedrill', 'beedrill'), ('pidgey', 'pidgey'), ('pidgeotto', 'pidgeotto'), ('pidgeot', 'pidgeot'), ('rattata', 'rattata'), ('raticate', 'raticate'), ('spearow', 'spearow'), ('fearow', 'fearow'), ('ekans', 'ekans'), ('arbok', 'arbok'), ('pikachu', 'pikachu'), ('raichu', 'raichu'), ('sandshrew', 'sandshrew'), ('sandslash', 'sandslash'), ('nidoran-f', 'nidoran-f'), ('nidorina', 'nidorina'), ('nidoqueen', 'nidoqueen'), ('nidoran-m', 'nidoran-m'), ('nidorino', 'nidorino'), ('nidoking', 'nidoking'), ('clefairy', 'clefairy'), ('clefable', 'clefable'), ('vulpix', 'vulpix'), ('ninetales', 'ninetales'), ('jigglypuff', 'jigglypuff'), ('wigglytuff', 'wigglytuff'), ('zubat', 'zubat'), ('golbat', 'golbat'), ('oddish', 'oddish'), ('gloom', 'gloom'), ('vileplume', 'vileplume'), ('paras', 'paras'), ('parasect', 'parasect'), ('venonat', 'venonat'), ('venomoth', 'venomoth'), ('diglett', 'diglett'), ('dugtrio', 'dugtrio'), ('meowth', 'meowth'), ('persian', 'persian'), ('psyduck', 'psyduck'), ('golduck', 'golduck'), ('mankey', 'mankey'), ('primeape', 'primeape'), ('growlithe', 'growlithe'), ('arcanine', 'arcanine'), ('poliwag', 'poliwag'), ('poliwhirl', 'poliwhirl'), ('poliwrath', 'poliwrath'), ('abra', 'abra'), ('kadabra', 'kadabra'), ('alakazam', 'alakazam'), ('machop', 'machop'), ('machoke', 'machoke'), ('machamp', 'machamp'), ('bellsprout', 'bellsprout'), ('weepinbell', 'weepinbell'), ('victreebel', 'victreebel'), ('tentacool', 'tentacool'), ('tentacruel', 'tentacruel'), ('geodude', 'geodude'), ('graveler', 'graveler'), ('golem', 'golem'), ('ponyta', 'ponyta'), ('rapidash', 'rapidash'), ('slowpoke', 'slowpoke'), ('slowbro', 'slowbro'), ('magnemite', 'magnemite'), ('magneton', 'magneton'), ('farfetchd', 'farfetchd'), ('doduo', 'doduo'), ('dodrio', 'dodrio'), ('seel', 'seel'), ('dewgong', 'dewgong'), ('grimer', 'grimer'), ('muk', 'muk'), ('shellder', 'shellder'), ('cloyster', 'cloyster'), ('gastly', 'gastly'), ('haunter', 'haunter'), ('gengar', 'gengar'), ('onix', 'onix'), ('drowzee', 'drowzee'), ('hypno', 'hypno'), ('krabby', 'krabby'), ('kingler', 'kingler'), ('voltorb', 'voltorb'), ('electrode', 'electrode'), ('exeggcute', 'exeggcute'), ('exeggutor', 'exeggutor'), ('cubone', 'cubone'), ('marowak', 'marowak'), ('hitmonlee', 'hitmonlee'), ('hitmonchan', 'hitmonchan'), ('lickitung', 'lickitung'), ('koffing', 'koffing'), ('weezing', 'weezing'), ('rhyhorn', 'rhyhorn'), ('rhydon', 'rhydon'), ('chansey', 'chansey'), ('tangela', 'tangela'), ('kangaskhan', 'kangaskhan'), ('horsea', 'horsea'), ('seadra', 'seadra'), ('goldeen', 'goldeen'), ('seaking', 'seaking'), ('staryu', 'staryu'), ('starmie', 'starmie'), ('mr-mime', 'mr-mime'), ('scyther', 'scyther'), ('jynx', 'jynx'), ('electabuzz', 'electabuzz'), ('magmar', 'magmar'), ('pinsir', 'pinsir'), ('tauros', 'tauros'), ('magikarp', 'magikarp'), ('gyarados', 'gyarados'), ('lapras', 'lapras'), ('ditto', 'ditto'), ('eevee', 'eevee'), ('vaporeon', 'vaporeon'), ('jolteon', 'jolteon'), ('flareon', 'flareon'), ('porygon', 'porygon'), ('omanyte', 'omanyte'), ('omastar', 'omastar'), ('kabuto', 'kabuto'), ('kabutops', 'kabutops'), ('aerodactyl', 'aerodactyl'), ('snorlax', 'snorlax'), ('articuno', 'articuno'), ('zapdos', 'zapdos'), ('moltres', 'moltres'), ('dratini', 'dratini'), ('dragonair', 'dragonair'), ('dragonite', 'dragonite'), ('mewtwo', 'mewtwo'), ('mew', 'mew'), ('chikorita', 'chikorita'), ('bayleef', 'bayleef'), ('meganium', 'meganium'), ('cyndaquil', 'cyndaquil'), ('quilava', 'quilava'), ('typhlosion', 'typhlosion'), ('totodile', 'totodile'), ('croconaw', 'croconaw'), ('feraligatr', 'feraligatr'), ('sentret', 'sentret'), ('furret', 'furret'), ('hoothoot', 'hoothoot'), ('noctowl', 'noctowl'), ('ledyba', 'ledyba'), ('ledian', 'ledian'), ('spinarak', 'spinarak'), ('ariados', 'ariados'), ('crobat', 'crobat'), ('chinchou', 'chinchou'), ('lanturn', 'lanturn'), ('pichu', 'pichu'), ('cleffa', 'cleffa'), ('igglybuff', 'igglybuff'), ('togepi', 'togepi'), ('togetic', 'togetic'), ('natu', 'natu'), ('xatu', 'xatu'), ('mareep', 'mareep'), ('flaaffy', 'flaaffy'), ('ampharos', 'ampharos'), ('bellossom', 'bellossom'), ('marill', 'marill'), ('azumarill', 'azumarill'), ('sudowoodo', 'sudowoodo'), ('politoed', 'politoed'), ('hoppip', 'hoppip'), ('skiploom', 'skiploom'), ('jumpluff', 'jumpluff'), ('aipom', 'aipom'), ('sunkern', 'sunkern'), ('sunflora', 'sunflora'), ('yanma', 'yanma'), ('wooper', 'wooper'), ('quagsire', 'quagsire'), ('espeon', 'espeon'), ('umbreon', 'umbreon'), ('murkrow', 'murkrow'), ('slowking', 'slowking'), ('misdreavus', 'misdreavus'), ('unown', 'unown'), ('wobbuffet', 'wobbuffet'), ('girafarig', 'girafarig'), ('pineco', 'pineco'), ('forretress', 'forretress'), ('dunsparce', 'dunsparce'), ('gligar', 'gligar'), ('steelix', 'steelix'), ('snubbull', 'snubbull'), ('granbull', 'granbull'), ('qwilfish', 'qwilfish'), ('scizor', 'scizor'), ('shuckle', 'shuckle'), ('heracross', 'heracross'), ('sneasel', 'sneasel'), ('teddiursa', 'teddiursa'), ('ursaring', 'ursaring'), ('slugma', 'slugma'), ('magcargo', 'magcargo'), ('swinub', 'swinub'), ('piloswine', 'piloswine'), ('corsola', 'corsola'), ('remoraid', 'remoraid'), ('octillery', 'octillery'), ('delibird', 'delibird'), ('mantine', 'mantine'), ('skarmory', 'skarmory'), ('houndour', 'houndour'), ('houndoom', 'houndoom'), ('kingdra', 'kingdra'), ('phanpy', 'phanpy'), ('donphan', 'donphan'), ('porygon2', 'porygon2'), ('stantler', 'stantler'), ('smeargle', 'smeargle'), ('tyrogue', 'tyrogue'), ('hitmontop', 'hitmontop'), ('smoochum', 'smoochum'), ('elekid', 'elekid'), ('magby', 'magby'), ('miltank', 'miltank'), ('blissey', 'blissey'), ('raikou', 'raikou'), ('entei', 'entei'), ('suicune', 'suicune'), ('larvitar', 'larvitar'), ('pupitar', 'pupitar'), ('tyranitar', 'tyranitar'), ('lugia', 'lugia'), ('ho-oh', 'ho-oh'), ('celebi', 'celebi'), ('treecko', 'treecko'), ('grovyle', 'grovyle'), ('sceptile', 'sceptile'), ('torchic', 'torchic'), ('combusken', 'combusken'), ('blaziken', 'blaziken'), ('mudkip', 'mudkip'), ('marshtomp', 'marshtomp'), ('swampert', 'swampert'), ('poochyena', 'poochyena'), ('mightyena', 'mightyena'), ('zigzagoon', 'zigzagoon'), ('linoone', 'linoone'), ('wurmple', 'wurmple'), ('silcoon', 'silcoon'), ('beautifly', 'beautifly'), ('cascoon', 'cascoon'), ('dustox', 'dustox'), ('lotad', 'lotad'), ('lombre', 'lombre'), ('ludicolo', 'ludicolo'), ('seedot', 'seedot'), ('nuzleaf', 'nuzleaf'), ('shiftry', 'shiftry'), ('taillow', 'taillow'), ('swellow', 'swellow'), ('wingull', 'wingull'), ('pelipper', 'pelipper'), ('ralts', 'ralts'), ('kirlia', 'kirlia'), ('gardevoir', 'gardevoir'), ('surskit', 'surskit'), ('masquerain', 'masquerain'), ('shroomish', 'shroomish'), ('breloom', 'breloom'), ('slakoth', 'slakoth'), ('vigoroth', 'vigoroth'), ('slaking', 'slaking'), ('nincada', 'nincada'), ('ninjask', 'ninjask'), ('shedinja', 'shedinja'), ('whismur', 'whismur'), ('loudred', 'loudred'), ('exploud', 'exploud'), ('makuhita', 'makuhita'), ('hariyama', 'hariyama'), ('azurill', 'azurill'), ('nosepass', 'nosepass'), ('skitty', 'skitty'), ('delcatty', 'delcatty'), ('sableye', 'sableye'), ('mawile', 'mawile'), ('aron', 'aron'), ('lairon', 'lairon'), ('aggron', 'aggron'), ('meditite', 'meditite'), ('medicham', 'medicham'), ('electrike', 'electrike'), ('manectric', 'manectric'), ('plusle', 'plusle'), ('minun', 'minun'), ('volbeat', 'volbeat'), ('illumise', 'illumise'), ('roselia', 'roselia'), ('gulpin', 'gulpin'), ('swalot', 'swalot'), ('carvanha', 'carvanha'), ('sharpedo', 'sharpedo'), ('wailmer', 'wailmer'), ('wailord', 'wailord'), ('numel', 'numel'), ('camerupt', 'camerupt'), ('torkoal', 'torkoal'), ('spoink', 'spoink'), ('grumpig', 'grumpig'), ('spinda', 'spinda'), ('trapinch', 'trapinch'), ('vibrava', 'vibrava'), ('flygon', 'flygon'), ('cacnea', 'cacnea'), ('cacturne', 'cacturne'), ('swablu', 'swablu'), ('altaria', 'altaria'), ('zangoose', 'zangoose'), ('seviper', 'seviper'), ('lunatone', 'lunatone'), ('solrock', 'solrock'), ('barboach', 'barboach'), ('whiscash', 'whiscash'), ('corphish', 'corphish'), ('crawdaunt', 'crawdaunt'), ('baltoy', 'baltoy'), ('claydol', 'claydol'), ('lileep', 'lileep'), ('cradily', 'cradily'), ('anorith', 'anorith'), ('armaldo', 'armaldo'), ('feebas', 'feebas'), ('milotic', 'milotic'), ('castform', 'castform'), ('kecleon', 'kecleon'), ('shuppet', 'shuppet'), ('banette', 'banette'), ('duskull', 'duskull'), ('dusclops', 'dusclops'), ('tropius', 'tropius'), ('chimecho', 'chimecho'), ('absol', 'absol'), ('wynaut', 'wynaut'), ('snorunt', 'snorunt'), ('glalie', 'glalie'), ('spheal', 'spheal'), ('sealeo', 'sealeo'), ('walrein', 'walrein'), ('clamperl', 'clamperl'), ('huntail', 'huntail'), ('gorebyss', 'gorebyss'), ('relicanth', 'relicanth'), ('luvdisc', 'luvdisc'), ('bagon', 'bagon'), ('shelgon', 'shelgon'), ('salamence', 'salamence'), ('beldum', 'beldum'), ('metang', 'metang'), ('metagross', 'metagross'), ('regirock', 'regirock'), ('regice', 'regice'), ('registeel', 'registeel'), ('latias', 'latias'), ('latios', 'latios'), ('kyogre', 'kyogre'), ('groudon', 'groudon'), ('rayquaza', 'rayquaza'), ('jirachi', 'jirachi'), ('deoxys-normal', 'deoxys-normal'), ('turtwig', 'turtwig'), ('grotle', 'grotle'), ('torterra', 'torterra'), ('chimchar', 'chimchar'), ('monferno', 'monferno'), ('infernape', 'infernape'), ('piplup', 'piplup'), ('prinplup', 'prinplup'), ('empoleon', 'empoleon'), ('starly', 'starly'), ('staravia', 'staravia'), ('staraptor', 'staraptor'), ('bidoof', 'bidoof'), ('bibarel', 'bibarel'), ('kricketot', 'kricketot'), ('kricketune', 'kricketune'), ('shinx', 'shinx'), ('luxio', 'luxio'), ('luxray', 'luxray'), ('budew', 'budew'), ('roserade', 'roserade'), ('cranidos', 'cranidos'), ('rampardos', 'rampardos'), ('shieldon', 'shieldon'), ('bastiodon', 'bastiodon'), ('burmy', 'burmy'), ('wormadam-plant', 'wormadam-plant'), ('mothim', 'mothim'), ('combee', 'combee'), ('vespiquen', 'vespiquen'), ('pachirisu', 'pachirisu'), ('buizel', 'buizel'), ('floatzel', 'floatzel'), ('cherubi', 'cherubi'), ('cherrim', 'cherrim'), ('shellos', 'shellos'), ('gastrodon', 'gastrodon'), ('ambipom', 'ambipom'), ('drifloon', 'drifloon'), ('drifblim', 'drifblim'), ('buneary', 'buneary'), ('lopunny', 'lopunny'), ('mismagius', 'mismagius'), ('honchkrow', 'honchkrow'), ('glameow', 'glameow'), ('purugly', 'purugly'), ('chingling', 'chingling'), ('stunky', 'stunky'), ('skuntank', 'skuntank'), ('bronzor', 'bronzor'), ('bronzong', 'bronzong'), ('bonsly', 'bonsly'), ('mime-jr', 'mime-jr'), ('happiny', 'happiny'), ('chatot', 'chatot'), ('spiritomb', 'spiritomb'), ('gible', 'gible'), ('gabite', 'gabite'), ('garchomp', 'garchomp'), ('munchlax', 'munchlax'), ('riolu', 'riolu'), ('lucario', 'lucario'), ('hippopotas', 'hippopotas'), ('hippowdon', 'hippowdon'), ('skorupi', 'skorupi'), ('drapion', 'drapion'), ('croagunk', 'croagunk'), ('toxicroak', 'toxicroak'), ('carnivine', 'carnivine'), ('finneon', 'finneon'), ('lumineon', 'lumineon'), ('mantyke', 'mantyke'), ('snover', 'snover'), ('abomasnow', 'abomasnow'), ('weavile', 'weavile'), ('magnezone', 'magnezone'), ('lickilicky', 'lickilicky'), ('rhyperior', 'rhyperior'), ('tangrowth', 'tangrowth'), ('electivire', 'electivire'), ('magmortar', 'magmortar'), ('togekiss', 'togekiss'), ('yanmega', 'yanmega'), ('leafeon', 'leafeon'), ('glaceon', 'glaceon'), ('gliscor', 'gliscor'), ('mamoswine', 'mamoswine'), ('porygon-z', 'porygon-z'), ('gallade', 'gallade'), ('probopass', 'probopass'), ('dusknoir', 'dusknoir'), ('froslass', 'froslass'), ('rotom', 'rotom'), ('uxie', 'uxie'), ('mesprit', 'mesprit'), ('azelf', 'azelf'), ('dialga', 'dialga'), ('palkia', 'palkia'), ('heatran', 'heatran'), ('regigigas', 'regigigas'), ('giratina-altered', 'giratina-altered'), ('cresselia', 'cresselia'), ('phione', 'phione'), ('manaphy', 'manaphy'), ('darkrai', 'darkrai'), ('shaymin-land', 'shaymin-land'), ('arceus', 'arceus'), ('victini', 'victini'), ('snivy', 'snivy'), ('servine', 'servine'), ('serperior', 'serperior'), ('tepig', 'tepig'), ('pignite', 'pignite'), ('emboar', 'emboar'), ('oshawott', 'oshawott'), ('dewott', 'dewott'), ('samurott', 'samurott'), ('patrat', 'patrat'), ('watchog', 'watchog'), ('lillipup', 'lillipup'), ('herdier', 'herdier'), ('stoutland', 'stoutland'), ('purrloin', 'purrloin'), ('liepard', 'liepard'), ('pansage', 'pansage'), ('simisage', 'simisage'), ('pansear', 'pansear'), ('simisear', 'simisear'), ('panpour', 'panpour'), ('simipour', 'simipour'), ('munna', 'munna'), ('musharna', 'musharna'), ('pidove', 'pidove'), ('tranquill', 'tranquill'), ('unfezant', 'unfezant'), ('blitzle', 'blitzle'), ('zebstrika', 'zebstrika'), ('roggenrola', 'roggenrola'), ('boldore', 'boldore'), ('gigalith', 'gigalith'), ('woobat', 'woobat'), ('swoobat', 'swoobat'), ('drilbur', 'drilbur'), ('excadrill', 'excadrill'), ('audino', 'audino'), ('timburr', 'timburr'), ('gurdurr', 'gurdurr'), ('conkeldurr', 'conkeldurr'), ('tympole', 'tympole'), ('palpitoad', 'palpitoad'), ('seismitoad', 'seismitoad'), ('throh', 'throh'), ('sawk', 'sawk'), ('sewaddle', 'sewaddle'), ('swadloon', 'swadloon'), ('leavanny', 'leavanny'), ('venipede', 'venipede'), ('whirlipede', 'whirlipede'), ('scolipede', 'scolipede'), ('cottonee', 'cottonee'), ('whimsicott', 'whimsicott'), ('petilil', 'petilil'), ('lilligant', 'lilligant'), ('basculin-red-striped', 'basculin-red-striped'), ('sandile', 'sandile'), ('krokorok', 'krokorok'), ('krookodile', 'krookodile'), ('darumaka', 'darumaka'), ('darmanitan-standard', 'darmanitan-standard'), ('maractus', 'maractus'), ('dwebble', 'dwebble'), ('crustle', 'crustle'), ('scraggy', 'scraggy'), ('scrafty', 'scrafty'), ('sigilyph', 'sigilyph'), ('yamask', 'yamask'), ('cofagrigus', 'cofagrigus'), ('tirtouga', 'tirtouga'), ('carracosta', 'carracosta'), ('archen', 'archen'), ('archeops', 'archeops'), ('trubbish', 'trubbish'), ('garbodor', 'garbodor'), ('zorua', 'zorua'), ('zoroark', 'zoroark'), ('minccino', 'minccino'), ('cinccino', 'cinccino'), ('gothita', 'gothita'), ('gothorita', 'gothorita'), ('gothitelle', 'gothitelle'), ('solosis', 'solosis'), ('duosion', 'duosion'), ('reuniclus', 'reuniclus'), ('ducklett', 'ducklett'), ('swanna', 'swanna'), ('vanillite', 'vanillite'), ('vanillish', 'vanillish'), ('vanilluxe', 'vanilluxe'), ('deerling', 'deerling'), ('sawsbuck', 'sawsbuck'), ('emolga', 'emolga'), ('karrablast', 'karrablast'), ('escavalier', 'escavalier'), ('foongus', 'foongus'), ('amoonguss', 'amoonguss'), ('frillish', 'frillish'), ('jellicent', 'jellicent'), ('alomomola', 'alomomola'), ('joltik', 'joltik'), ('galvantula', 'galvantula'), ('ferroseed', 'ferroseed'), ('ferrothorn', 'ferrothorn'), ('klink', 'klink'), ('klang', 'klang'), ('klinklang', 'klinklang'), ('tynamo', 'tynamo'), ('eelektrik', 'eelektrik'), ('eelektross', 'eelektross'), ('elgyem', 'elgyem'), ('beheeyem', 'beheeyem'), ('litwick', 'litwick'), ('lampent', 'lampent'), ('chandelure', 'chandelure'), ('axew', 'axew'), ('fraxure', 'fraxure'), ('haxorus', 'haxorus'), ('cubchoo', 'cubchoo'), ('beartic', 'beartic'), ('cryogonal', 'cryogonal'), ('shelmet', 'shelmet'), ('accelgor', 'accelgor'), ('stunfisk', 'stunfisk'), ('mienfoo', 'mienfoo'), ('mienshao', 'mienshao'), ('druddigon', 'druddigon'), ('golett', 'golett'), ('golurk', 'golurk'), ('pawniard', 'pawniard'), ('bisharp', 'bisharp'), ('bouffalant', 'bouffalant'), ('rufflet', 'rufflet'), ('braviary', 'braviary'), ('vullaby', 'vullaby'), ('mandibuzz', 'mandibuzz'), ('heatmor', 'heatmor'), ('durant', 'durant'), ('deino', 'deino'), ('zweilous', 'zweilous'), ('hydreigon', 'hydreigon'), ('larvesta', 'larvesta'), ('volcarona', 'volcarona'), ('cobalion', 'cobalion'), ('terrakion', 'terrakion'), ('virizion', 'virizion'), ('tornadus-incarnate', 'tornadus-incarnate'), ('thundurus-incarnate', 'thundurus-incarnate'), ('reshiram', 'reshiram'), ('zekrom', 'zekrom'), ('landorus-incarnate', 'landorus-incarnate'), ('kyurem', 'kyurem'), ('keldeo-ordinary', 'keldeo-ordinary'), ('meloetta-aria', 'meloetta-aria'), ('genesect', 'genesect'), ('chespin', 'chespin'), ('quilladin', 'quilladin'), ('chesnaught', 'chesnaught'), ('fennekin', 'fennekin'), ('braixen', 'braixen'), ('delphox', 'delphox'), ('froakie', 'froakie'), ('frogadier', 'frogadier'), ('greninja', 'greninja'), ('bunnelby', 'bunnelby'), ('diggersby', 'diggersby'), ('fletchling', 'fletchling'), ('fletchinder', 'fletchinder'), ('talonflame', 'talonflame'), ('scatterbug', 'scatterbug'), ('spewpa', 'spewpa'), ('vivillon', 'vivillon'), ('litleo', 'litleo'), ('pyroar', 'pyroar'), ('flabebe', 'flabebe'), ('floette', 'floette'), ('florges', 'florges'), ('skiddo', 'skiddo'), ('gogoat', 'gogoat'), ('pancham', 'pancham'), ('pangoro', 'pangoro'), ('furfrou', 'furfrou'), ('espurr', 'espurr'), ('meowstic-male', 'meowstic-male'), ('honedge', 'honedge'), ('doublade', 'doublade'), ('aegislash-shield', 'aegislash-shield'), ('spritzee', 'spritzee'), ('aromatisse', 'aromatisse'), ('swirlix', 'swirlix'), ('slurpuff', 'slurpuff'), ('inkay', 'inkay'), ('malamar', 'malamar'), ('binacle', 'binacle'), ('barbaracle', 'barbaracle'), ('skrelp', 'skrelp'), ('dragalge', 'dragalge'), ('clauncher', 'clauncher'), ('clawitzer', 'clawitzer'), ('helioptile', 'helioptile'), ('heliolisk', 'heliolisk'), ('tyrunt', 'tyrunt'), ('tyrantrum', 'tyrantrum'), ('amaura', 'amaura'), ('aurorus', 'aurorus'), ('sylveon', 'sylveon'), ('hawlucha', 'hawlucha'), ('dedenne', 'dedenne'), ('carbink', 'carbink'), ('goomy', 'goomy'), ('sliggoo', 'sliggoo'), ('goodra', 'goodra'), ('klefki', 'klefki'), ('phantump', 'phantump'), ('trevenant', 'trevenant'), ('pumpkaboo-average', 'pumpkaboo-average'), ('gourgeist-average', 'gourgeist-average'), ('bergmite', 'bergmite'), ('avalugg', 'avalugg'), ('noibat', 'noibat'), ('noivern', 'noivern'), ('xerneas', 'xerneas'), ('yveltal', 'yveltal'), ('zygarde', 'zygarde'), ('diancie', 'diancie'), ('hoopa', 'hoopa'), ('volcanion', 'volcanion'), ('rowlet', 'rowlet'), ('dartrix', 'dartrix'), ('decidueye', 'decidueye'), ('litten', 'litten'), ('torracat', 'torracat'), ('incineroar', 'incineroar'), ('popplio', 'popplio'), ('brionne', 'brionne'), ('primarina', 'primarina'), ('pikipek', 'pikipek'), ('trumbeak', 'trumbeak'), ('toucannon', 'toucannon'), ('yungoos', 'yungoos'), ('gumshoos', 'gumshoos'), ('grubbin', 'grubbin'), ('charjabug', 'charjabug'), ('vikavolt', 'vikavolt'), ('crabrawler', 'crabrawler'), ('crabominable', 'crabominable'), ('oricorio-baile', 'oricorio-baile'), ('cutiefly', 'cutiefly'), ('ribombee', 'ribombee'), ('rockruff', 'rockruff'), ('lycanroc-midday', 'lycanroc-midday'), ('wishiwashi-solo', 'wishiwashi-solo'), ('mareanie', 'mareanie'), ('toxapex', 'toxapex'), ('mudbray', 'mudbray'), ('mudsdale', 'mudsdale'), ('dewpider', 'dewpider'), ('araquanid', 'araquanid'), ('fomantis', 'fomantis'), ('lurantis', 'lurantis'), ('morelull', 'morelull'), ('shiinotic', 'shiinotic'), ('salandit', 'salandit'), ('salazzle', 'salazzle'), ('stufful', 'stufful'), ('bewear', 'bewear'), ('bounsweet', 'bounsweet'), ('steenee', 'steenee'), ('tsareena', 'tsareena'), ('comfey', 'comfey'), ('oranguru', 'oranguru'), ('passimian', 'passimian'), ('wimpod', 'wimpod'), ('golisopod', 'golisopod'), ('sandygast', 'sandygast'), ('palossand', 'palossand'), ('pyukumuku', 'pyukumuku'), ('type-null', 'type-null'), ('silvally', 'silvally'), ('minior-red-meteor', 'minior-red-meteor'), ('komala', 'komala'), ('turtonator', 'turtonator'), ('togedemaru', 'togedemaru'), ('mimikyu-disguised', 'mimikyu-disguised'), ('bruxish', 'bruxish'), ('drampa', 'drampa'), ('dhelmise', 'dhelmise'), ('jangmo-o', 'jangmo-o'), ('hakamo-o', 'hakamo-o'), ('kommo-o', 'kommo-o'), ('tapu-koko', 'tapu-koko'), ('tapu-lele', 'tapu-lele'), ('tapu-bulu', 'tapu-bulu'), ('tapu-fini', 'tapu-fini'), ('cosmog', 'cosmog'), ('cosmoem', 'cosmoem'), ('solgaleo', 'solgaleo'), ('lunala', 'lunala'), ('nihilego', 'nihilego'), ('buzzwole', 'buzzwole'), ('pheromosa', 'pheromosa'), ('xurkitree', 'xurkitree'), ('celesteela', 'celesteela'), ('kartana', 'kartana'), ('guzzlord', 'guzzlord'), ('necrozma', 'necrozma'), ('magearna', 'magearna'), ('marshadow', 'marshadow'), ('poipole', 'poipole'), ('naganadel', 'naganadel'), ('stakataka', 'stakataka'), ('blacephalon', 'blacephalon'), ('zeraora', 'zeraora'), ('meltan', 'meltan'), ('melmetal', 'melmetal'), ('grookey', 'grookey'), ('thwackey', 'thwackey'), ('rillaboom', 'rillaboom'), ('scorbunny', 'scorbunny'), ('raboot', 'raboot'), ('cinderace', 'cinderace'), ('sobble', 'sobble'), ('drizzile', 'drizzile'), ('inteleon', 'inteleon'), ('skwovet', 'skwovet'), ('greedent', 'greedent'), ('rookidee', 'rookidee'), ('corvisquire', 'corvisquire'), ('corviknight', 'corviknight'), ('blipbug', 'blipbug'), ('dottler', 'dottler'), ('orbeetle', 'orbeetle'), ('nickit', 'nickit'), ('thievul', 'thievul'), ('gossifleur', 'gossifleur'), ('eldegoss', 'eldegoss'), ('wooloo', 'wooloo'), ('dubwool', 'dubwool'), ('chewtle', 'chewtle'), ('drednaw', 'drednaw'), ('yamper', 'yamper'), ('boltund', 'boltund'), ('rolycoly', 'rolycoly'), ('carkol', 'carkol'), ('coalossal', 'coalossal'), ('applin', 'applin'), ('flapple', 'flapple'), ('appletun', 'appletun'), ('silicobra', 'silicobra'), ('sandaconda', 'sandaconda'), ('cramorant', 'cramorant'), ('arrokuda', 'arrokuda'), ('barraskewda', 'barraskewda'), ('toxel', 'toxel'), ('toxtricity-amped', 'toxtricity-amped'), ('sizzlipede', 'sizzlipede'), ('centiskorch', 'centiskorch'), ('clobbopus', 'clobbopus'), ('grapploct', 'grapploct'), ('sinistea', 'sinistea'), ('polteageist', 'polteageist'), ('hatenna', 'hatenna'), ('hattrem', 'hattrem'), ('hatterene', 'hatterene'), ('impidimp', 'impidimp'), ('morgrem', 'morgrem'), ('grimmsnarl', 'grimmsnarl'), ('obstagoon', 'obstagoon'), ('perrserker', 'perrserker'), ('cursola', 'cursola'), ('sirfetchd', 'sirfetchd'), ('mr-rime', 'mr-rime'), ('runerigus', 'runerigus'), ('milcery', 'milcery'), ('alcremie', 'alcremie'), ('falinks', 'falinks'), ('pincurchin', 'pincurchin'), ('snom', 'snom'), ('frosmoth', 'frosmoth'), ('stonjourner', 'stonjourner'), ('eiscue-ice', 'eiscue-ice'), ('indeedee-male', 'indeedee-male'), ('morpeko', 'morpeko'), ('cufant', 'cufant'), ('copperajah', 'copperajah'), ('dracozolt', 'dracozolt'), ('arctozolt', 'arctozolt'), ('dracovish', 'dracovish'), ('arctovish', 'arctovish'), ('duraludon', 'duraludon'), ('dreepy', 'dreepy'), ('drakloak', 'drakloak'), ('dragapult', 'dragapult'), ('zacian-hero', 'zacian-hero'), ('zamazenta-hero', 'zamazenta-hero'), ('eternatus', 'eternatus'), ('kubfu', 'kubfu'), ('urshifu-single-strike', 'urshifu-single-strike'), ('zarude', 'zarude'), ('regieleki', 'regieleki'), ('regidrago', 'regidrago'), ('glastrier', 'glastrier'), ('spectrier', 'spectrier'), ('calyrex', 'calyrex'), ('deoxys-attack', 'deoxys-attack'), ('deoxys-defense', 'deoxys-defense'), ('deoxys-speed', 'deoxys-speed'), ('wormadam-sandy', 'wormadam-sandy'), ('wormadam-trash', 'wormadam-trash'), ('shaymin-sky', 'shaymin-sky'), ('giratina-origin', 'giratina-origin'), ('rotom-heat', 'rotom-heat'), ('rotom-wash', 'rotom-wash'), ('rotom-frost', 'rotom-frost'), ('rotom-fan', 'rotom-fan'), ('rotom-mow', 'rotom-mow'), ('castform-sunny', 'castform-sunny'), ('castform-rainy', 'castform-rainy'), ('castform-snowy', 'castform-snowy'), ('basculin-blue-striped', 'basculin-blue-striped'), ('darmanitan-zen', 'darmanitan-zen'), ('meloetta-pirouette', 'meloetta-pirouette'), ('tornadus-therian', 'tornadus-therian'), ('thundurus-therian', 'thundurus-therian'), ('landorus-therian', 'landorus-therian'), ('kyurem-black', 'kyurem-black'), ('kyurem-white', 'kyurem-white'), ('keldeo-resolute', 'keldeo-resolute'), ('meowstic-female', 'meowstic-female'), ('aegislash-blade', 'aegislash-blade'), ('pumpkaboo-small', 'pumpkaboo-small'), ('pumpkaboo-large', 'pumpkaboo-large'), ('pumpkaboo-super', 'pumpkaboo-super'), ('gourgeist-small', 'gourgeist-small'), ('gourgeist-large', 'gourgeist-large'), ('gourgeist-super', 'gourgeist-super'), ('venusaur-mega', 'venusaur-mega'), ('charizard-mega-x', 'charizard-mega-x'), ('charizard-mega-y', 'charizard-mega-y'), ('blastoise-mega', 'blastoise-mega'), ('alakazam-mega', 'alakazam-mega'), ('gengar-mega', 'gengar-mega'), ('kangaskhan-mega', 'kangaskhan-mega'), ('pinsir-mega', 'pinsir-mega'), ('gyarados-mega', 'gyarados-mega'), ('aerodactyl-mega', 'aerodactyl-mega'), ('mewtwo-mega-x', 'mewtwo-mega-x'), ('mewtwo-mega-y', 'mewtwo-mega-y'), ('ampharos-mega', 'ampharos-mega'), ('scizor-mega', 'scizor-mega'), ('heracross-mega', 'heracross-mega'), ('houndoom-mega', 'houndoom-mega'), ('tyranitar-mega', 'tyranitar-mega'), ('blaziken-mega', 'blaziken-mega'), ('gardevoir-mega', 'gardevoir-mega'), ('mawile-mega', 'mawile-mega'), ('aggron-mega', 'aggron-mega'), ('medicham-mega', 'medicham-mega'), ('manectric-mega', 'manectric-mega'), ('banette-mega', 'banette-mega'), ('absol-mega', 'absol-mega'), ('garchomp-mega', 'garchomp-mega'), ('lucario-mega', 'lucario-mega'), ('abomasnow-mega', 'abomasnow-mega'), ('floette-eternal', 'floette-eternal'), ('latias-mega', 'latias-mega'), ('latios-mega', 'latios-mega'), ('swampert-mega', 'swampert-mega'), ('sceptile-mega', 'sceptile-mega'), ('sableye-mega', 'sableye-mega'), ('altaria-mega', 'altaria-mega'), ('gallade-mega', 'gallade-mega'), ('audino-mega', 'audino-mega'), ('sharpedo-mega', 'sharpedo-mega'), ('slowbro-mega', 'slowbro-mega'), ('steelix-mega', 'steelix-mega'), ('pidgeot-mega', 'pidgeot-mega'), ('glalie-mega', 'glalie-mega'), ('diancie-mega', 'diancie-mega'), ('metagross-mega', 'metagross-mega'), ('kyogre-primal', 'kyogre-primal'), ('groudon-primal', 'groudon-primal'), ('rayquaza-mega', 'rayquaza-mega'), ('pikachu-rock-star', 'pikachu-rock-star'), ('pikachu-belle', 'pikachu-belle'), ('pikachu-pop-star', 'pikachu-pop-star'), ('pikachu-phd', 'pikachu-phd'), ('pikachu-libre', 'pikachu-libre'), ('pikachu-cosplay', 'pikachu-cosplay'), ('hoopa-unbound', 'hoopa-unbound'), ('camerupt-mega', 'camerupt-mega'), ('lopunny-mega', 'lopunny-mega'), ('salamence-mega', 'salamence-mega'), ('beedrill-mega', 'beedrill-mega'), ('rattata-alola', 'rattata-alola'), ('raticate-alola', 'raticate-alola'), ('raticate-totem-alola', 'raticate-totem-alola'), ('pikachu-original-cap', 'pikachu-original-cap'), ('pikachu-hoenn-cap', 'pikachu-hoenn-cap'), ('pikachu-sinnoh-cap', 'pikachu-sinnoh-cap'), ('pikachu-unova-cap', 'pikachu-unova-cap'), ('pikachu-kalos-cap', 'pikachu-kalos-cap'), ('pikachu-alola-cap', 'pikachu-alola-cap'), ('raichu-alola', 'raichu-alola'), ('sandshrew-alola', 'sandshrew-alola'), ('sandslash-alola', 'sandslash-alola')], max_length=200, null=True, verbose_name='Pokemon 3:'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='player1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='What is your name?'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='player2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Choose your opponent:'),
        ),
    ]
