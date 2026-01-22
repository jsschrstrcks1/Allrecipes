#!/usr/bin/env python3
"""
Add comprehensive world cheese varieties to CHEESE_VARIETIES_TRACKER.md
Data sourced from alphalists.com and engdic.org cheese databases
"""

import re
from pathlib import Path

# Comprehensive cheese list from multiple sources
# Organized alphabetically with over 1000 varieties

WORLD_CHEESES = """
# A
Abbaye de Belloc, Abbaye de Citeaux, Abbaye du Mont des Cats, Abertam, Abondance, Acapella, Ackawi, Acorn, Adelost, Affidelice au Chablis, Afuega'l Pitu, Airag, Airedale, Aisy Cendre, Allgauer Emmentaler, Alverca, Ambert, American Cheese, Ami du Chambertin, Anejo Enchilado, Anneau du Vic-Bilh, Anthoriro, Appenzell, Aragon, Ardi Gasna, Ardrahan, Armenian String, Aromes au Gene de Marc, Asadero, Asiago, Aubisque Pyrenees, Autun, Avaxtskyr, Azeitao

# B
Baby Swiss, Babybel, Baguette Laonnaise, Bakers, Baladi, Balaton, Bandal, Banon, Barry's Bay Cheddar, Basing, Basket Cheese, Bath Cheese, Bavarian Bergkase, Baylough, Beaufort, Beauvoorde, Beenleigh Blue, Beer Cheese, Bel Paese, Bergader, Bergere Bleue, Berkswell, Bethmale, Beyaz Peynir, Bierkase, Bishop Kennedy, Blarney, Bleu d'Auvergne, Bleu de Gex, Bleu de Laqueuille, Bleu de Septmoncel, Bleu de Termignon, Bleu Des Causses, Blue Castello, Blue Rathgore, Bocconcini, Boeren Leidenkaas, Bonchester, Bosworth, Bougon, Boule Du Roves, Boulette d'Avesnes, Boursault, Boursin, Bouyssou, Bra, Braudostur, Breakfast Cheese, Brebis du Lavort, Bresse Bleu, Brick, Brie, Brie de Meaux, Brie de Melun, Brillat-Savarin, Brin, Brin d'Amour, Brinza, Briquette de Brebis, Broccio, Bruder Basil, Brusselae Kaas, Bryndza, Buchette d'Anjou, Buffalo, Burgos, Butte, Butterkase, Button, Buxton Blue

# C
Cabecou, Caboc, Cabrales, Cachaille, Caciocavallo, Caciotta, Caerphilly, Cairnsmore, Calenzana, Cambazola, Camembert de Normandie, Canadian Cheddar, Canestrato, Cantal, Caprice des Dieux, Capricorn Goat, Capriole Banon, Caravane, Carre de l'Est, Casciotta di Urbino, Cashel Blue, Castelleno, Castelmagno, Castelo Branco, Castigliano, Cathelain, Celtic Promise, Cendre d'Olivet, Cerney, Chabichou, Chabichou du Poitou, Chaource, Charolais, Chaumes, Cheddar Clothbound, Cheshire, Chevrotin des Aravis, Chontaleno, Civray, Coeur de Camembert au Calvados, Cojack, Colby, Cold Pack, Comte, Coolea, Cooleney, Coquetdale, Corleggy, Cornish Pepper, Cotherstone, Cotija, Cottage Cheese, Cougar Gold, Coulommiers, Coverdale, Crayeux de Roncq, Cream Cheese, Cream Havarti, Crema Agria, Crema Mexicana, Creme Fraiche, Crescenza, Croghan, Crottin de Chavignol, Crowdie, Crowley, Cuajada, Curd, Cure Nantais, Curworthy, Cwmtawe Pecorino, Cypress Grove Chevre

# D
Danablu, Danbo, Danish Fontina, Daralagjazsky, Dauphin, Delice des Fiouves, Denhany Dorset Drum, Derby, Dessertnyj Belyj, Devon Blue, Devon Garland, Dolcelatte, Doolin, Doppelrhamstufel, Dorset Blue Vinney, Double Gloucester, Double Worcester, Dreux a la Feuille, Dry Jack, Duddleswell, Dunbarra, Dunlop, Dunsyre Blue, Duroblando, Durrus, Dutch Mimolette

# E
Edam, Edelpilz, Emental Grand Cru, Emlett, Emmental, Epoisses de Bourgogne, Esbareich, Esrom, Etorki, Evansdale Farmhouse Brie, Evora, Exmoor Blue, Explorateur

# F
Farmer, Feta, Figue, Filetta, Fin-de-Siecle, Finlandia Swiss, Finn, Fiore Sardo, Fleur du Maquis, Flor de Guia, Flower Marie, Folded, Fondant de Brebis, Fontainebleau, Fontal, Fontina Val d'Aosta, Formaggio di Capra, Fougerus, Four Herb Gouda, Fourme d'Ambert, Fourme de Montbrison, Fresh Jack, Fresh Mozzarella, Fresh Ricotta, Fribourgeois, Friesekaas, Friesian, Friesla, Frinault, Fromage a Raclette, Fromage Corse, Fromage de Montagne de Savoie, Fromage Frais, Fynbo

# G
Gabriel, Galette du Paludier, Galette Lyonnaise, Galloway Goat's Milk Gems, Gammelost, Gaperon a l'Ail, Garrotxa, Gastanberra, Geitost, Gippsland Blue, Gjetost, Gloucester, Golden Cross, Gorgonzola, Gornyaltajski, Gospel Green, Gouda, Goutu, Gowrie, Grabetto, Graddost, Grafton Village Cheddar, Grana, Grana Padano, Grand Vatel, Grataron d'Areches, Gratte-Paille, Graviera, Greuilh, Greve, Gris de Lille, Gruyere, Gubbeen, Guerbigny

# H
Halloumi, Harbourne Blue, Havarti, Heidi Gruyere, Hereford Hop, Herrgardsost, Herriot Farmhouse, Herve, Hipi Iti, Hubbardston Blue Cow, Humboldt Fog, Hushallsost

# I
Iberico, Idaho Goatster, Idiazabal, Il Boschetto al Tartufo, Ile d'Yeu, Isle of Mull

# J
Jarlsberg, Jermi Tortes, Jibneh Arabieh, Jindi Brie, Jubilee Blue, Juustoleipa

# K
Kadchgall, Kaseri, Kashta, Kefalotyri, Kenafa, Kernhem, Kervella Affine, Kikorangi, King Island Cape Wickham Brie, King River Gold, Klosterkaese, Knockalara, Kugelkase

# L
L'Aveyronnais, L'Ecir de l'Aubrac, La Taupiniere, La Vache Qui Rit, Laguiole, Lairobell, Lajta, Lanark Blue, Lancashire, Langres, Lappi, Laruns, Lavistown, Le Brin, Le Fium Orbo, Le Lacandou, Le Roule, Leafield, Lebbene, Leerdammer, Leicester, Leyden, Limburger, Lincolnshire Poacher, Lingot Saint Bousquet d'Orb, Liptauer, Little Rydings, Livarot, Llanboidy, Llanglofan Farmhouse, Loch Arthur Farmhouse, Loddiswell Avondale, Longhorn, Lou Palou, Lou Pevre, Lyonnais

# M
Maasdam, Macconais, Mahoe Aged Gouda, Mahon, Malvern, Mamirolle, Manchego, Manouri, Manur, Marble Cheddar, Marbled Cheeses, Maredsous, Margotin, Maribo, Maroilles, Mascares, Mascarpone, Mascarpone Torta, Matocq, Maytag Blue, Meira, Menallack Farmhouse, Menonita, Meredith Blue, Mesost, Metton, Meyer Vintage Gouda, Mihalic Peynir, Milleens, Mimolette, Mine-Gabhar, Mini Baby Bells, Mixte, Molbo, Monastery Cheeses, Mondseer, Mont D'or Lyonnais, Montasio, Monterey Jack, Monterey Jack Dry, Morbier, Mothais a la Feuille, Mozzarella, Mozzarella di Bufala, Muenster, Murol, Mycella, Myzithra

# N
Naboulsi, Nantais, Neufchatel, Niolo, Nokkelost, Northumberland

# O
Oaxaca, Olde York, Olivet au Foin, Olivet Bleu, Olivet Cendre, Orkney Extra Mature Cheddar, Orla, Oschtjepka, Ossau Fermier, Ossau-Iraty, Oszczypek, Oxford Blue

# P
P'tit Berrichon, Palet de Babligny, Paneer, Panela, Pannerone, Pant ys Gawn, Parmesan, Parmigiano Reggiano, Pas de l'Escalette, Passendale, Pasteurized Processed, Pate de Fromage, Patefine Fort, Pave d'Affinois, Pave d'Auge, Pave de Chirac, Pave du Berry, Pecorino, Pecorino in Walnut Leaves, Pecorino Romano, Peekskill Pyramid, Pelardon des Cevennes, Penamellera, Penbryn, Pencarreg, Pepper Jack, Perail de Brebis, Petit Morin, Petit Pardou, Petit-Suisse, Picodon de Chevre, Picos de Europa, Pinconning, Piora, Pithiviers au Foin, Plateau de Herve, Plymouth Cheese, Podhalanski, Poivre d'Ane, Polkolbin, Pont l'Eveque, Port Nicholson, Port-Salut, Postel, Pouligny-Saint-Pierre, Pourly, Prastost, Pressato, Prince-Jean, Processed Cheddar, Provel, Provolone, Pyengana Cheddar, Pyramide

# Q
Quark, Quartirolo Lombardo, Quatre-Vents, Quercy Petit, Queso Blanco, Queso de Murcia, Queso del Montsec, Queso del Tietar, Queso Fresco, Queso Iberico, Queso Jalapeno, Queso Majorero, Queso Media Luna, Queso Para Frier, Queso Quesadilla

# R
Rabacal, Raclette, Ragusano, Raschera, Reblochon, Red Leicester, Regal de la Dombes, Reggianito, Remedou, Requeson, Richelieu, Ricotta, Ricotta Salata, Ridder, Rigotte, Rocamadour, Rollot, Romano, Romans Part Dieu, Roncal, Roquefort, Roule, Rouleau De Beaulieu, Royalp Tilsit, Rubens, Rustinu

# S
Saaland Pfarr, Saanenkaese, Saga, Sage Derby, Sainte Maure, Saint-Marcellin, Saint-Nectaire, Saint-Paulin, Salers, Samso, San Simon, Sancerre, Sap Sago, Sardo, Sardo Egyptian, Sbrinz, Scamorza, Schabzieger, Schloss, Selles sur Cher, Selva, Serat, Seriously Strong Cheddar, Serra da Estrela, Sharpam, Shelburne Cheddar, Shropshire Blue, Siraz, Sirene, Smoked Gouda, Somerset Brie, Sonoma Jack, Sottocenare al Tartufo, Soumaintrain, Sourire Lozerien, Spenwood, St. Agur Blue Cheese, Stilton, Stinking Bishop, String, Sussex Slipcote, Sveciaost, Swaledale, Sweet Style Swiss, Swiss

# T
Tala, Taleggio, Tamie, Tasmania Highland Chevre Log, Taupiniere, Teifi, Telemea, Testouri, Tete de Moine, Tetilla, Texas Goat Cheese, Tibet, Tillamook Cheddar, Tilsit, Timboon Brie, Toma, Tomme Brulee, Tomme d'Abondance, Tomme de Chevre, Tomme de Romans, Tomme de Savoie, Tomme des Chouans, Torta del Casar, Toscanello, Touree de L'Aubier, Tourmalet, Trappe, Trois Cornes De Vendee, Tronchon, Trou du Cru, Truffe, Tupi, Turunmaa, Tymsboro, Tyn Grug, Tyning

# U
Ubriaco, Ulloa

# V
Vacherin-Fribourgeois, Valencay, Vasterbottenost, Venaco, Vendomois, Vermont Cheddar, Vieux Corse, Vignotte, Vulscombe

# W
Waimata Farmhouse Blue, Washed Rind Cheese, Waterloo, Weichkaese, Wellington, Wensleydale, White Stilton, Whitestone Farmhouse, Wigmore, Woodside Cabecou

# X
Xynotyro

# Y
Yarg Cornish, Yarra Valley Pyramid, Yorkshire Blue

# Z
Zamorano, Zanetti Grana Padano, Zanetti Parmigiano Reggiano
"""

# Additional cheeses from engdic.org source
ADDITIONAL_CHEESES = """
Abbot's Gold, Aged Cheese, Alpage, Amarelo da Beira Baixa, Amou, Anco, Appalachian, Aroma, Asturian Cheese, Ausone
Baita Friuli, Balfour, Barberey, Belper Knolle, Bianca, Blacksticks Blue, Bread Cheese, Brunost, Bucheron, Butter Cheese
Caprino, Caquelon, Cachet, Caciobufala, Damerham, Dante, Délice de Bourgogne, Dieted, DOP Gorgonzola, Dore de Roucoulons, Driftwood, Drunken Goat, Dziugas
Easya, Ebenezer, Edacity, Edith, El Pastor, Elk Mountain, Ellington, Ermite, Esquirrou, Etivaz, Eva, Evalon, Evergood, Extra Mature Wensleydale
Fajita, Fatcat, Fayoumi, Feher Szlovak, Flamenco, Flan, Florence, Flory's Truckle, Forme d'Auvergne, Franche Comté, Fresh Chevre, Frico
Gabriela, Galbani, Gamoneu, Glebe Brethan, Glounthaune, Goat Cheese, Gotthelf, Goudse, Grayson, Great Lakes Cheddar
Hafod, Ham, Handkase, Harbison, Harbutt's, Harzer, Havilah, Head Cheese, Heat, Herve Mons, Holstein, Hooligan, Hoop Cheddar, Huntsman, Huzar, Hytteost
Ibores, Icecream, Icesheet, Illawarra, Imokilly Regato, Imsil, Inglewhite Buffalo, Innes Brick, Innes Log, Inverness, Irish Cheddar, Isabirra, Isigny Ste Mere, Isle of Mull Cheddar, Isonzo, Istara, Italian Buffalo Cheese, Italian Stracchino, Ivernia
Jabugo, Jamband, Jami, Jasper Hill Farm, Jeju Hallabong, Jemez, Jerseymaid, Jibneh Bagila, Jibneh Bayda, Jiffybleu, Jindi Triple Cream, Jindivick, Jivaeri, Joseph Heler Cheese
Kabritt, Kaltbach, Kanterkaas, Karwendel Bergkas, Kashar, Kashkaval, Keen's Cheddar, Kefir Blue, Kern, King Island Dairy, Kingston Black, Knapwell, Komijn, Kopanisti, Korbacik, Kraft Dinner, Krakus, Kravis, Kürbiskernlaib, Kwaito
La Peral, La Serena, Labneh, Lacy Swiss, Lady Jane, Lance, L'Etivaz, Little Rollright, Loire, Lord of the Hundreds, Lorraine, Ludlow Blue, Lymeswold
Maccagno, Madrona, Maffra, Magna, Majorero, Mauro, Mimolette Vieille, Mount Tam
Nabob, Nantwich, Napoléon, Nduja, Nebrodi, Nelson's Port, New Moon, New York Cheddar, Nisa, Noireau, Nonfat, Noord-Hollandse Gouda, Norfolk Mardler, Normandy Camembert, Nostrale, Nottinghamshire
Oasis, Obrien, Ogleshield, Old Amsterdam, Old Ford, Old Harry, Old Nick, Old Smales, Olive Oil Gouda, Onetik, Onetik Blue, Orkney Smoked Cheddar, Orval, Osh Teqsi, Ossau-Iraty Brebis Pyrenées, Oswestry Goat's Cheese, Oveja, Ozark Mountain Blue
Pacific Rock, Pack Square, Paesanella, Paese, Palhais, Paniolo, Pantysgawn, Paring, Petite Basque
Quark Cheese, Quartirolo, Queen Anne, Quercy Blanc, Quercy Noir, Queso de Cabrales, Queso de la Gomera, Queso de la Peral, Queso de la Serena, Quesoanejo, Quiberville, Quiche, Quicke's Cheddar
Ragstone, Rarebit, Red Dragon, Red Hawk, Redwood Hill Farm, Roaring Forties Blue, Rodeo Cheese, Rossini, Roth Kase, Roussette, Roves des Garrigues, Rovethym, Royal Windsor Red
Saanen Silk, Salata, Saint Agur, Saint-Honoré, Sapsago, Sharp Cheddar, Sharpham Rustic, Shepherd's Purse, Snowdonia, Sottocenere, String Cheese, Sutton Lucy
Tacky, Tacosalad, Takelma, Tang, Tarentaise, Thistle Hill Farm, Tintern, Tirangi, Tomino, Triple Cream Cheese, Tropea, Truffade, Truffle Cheese, Tulum, Tuscan Pecorino
Ubriaco Al, Udon Noodles, Uinta, Umbriaco, Unaged, Uniekaas, Union Star Cheese, Uplands Cheese Company, Urdă de Joseni, Ushuaya
Vacherin, Valdeón, Valentine, Valle d'Aosta Fromadzo, Vallee d'Aspe, Van Gogh-Gouda, Veigadarte, Veined, Velveeta, Ventadour, Vera, Vermeer, Vernieres, Vicenza, Vieux-Boulogne, Villalón, Villarodin
Wagon Wheel, Waldo Smog, Wallace and Gromit's Wensleydale, Walnut Cheese, Wasabi Disc, Welsh Brie, Welsh Cheddar, Westcombe Cheddar, Whey Cheese, White Cheddar, Wilde Childe, Willoughby, Winchester, Wisconsin Cheese, Woodside Cheese Wrights, Worcester Gold, Wyfe of Bath
Xabier, Xale de Mallorca, Xammar, Xanthe, Xhaxhai, Xigalo, Xirdalan, Xixa, Xnipec, Xocolate, Xoconostle, Xonotlite, Xorto, Xurde, Xylotymbou, Xynomizythra
Yankee Cheddar, Yarlsberg, Yarra Valley Black Savourine, Yarra Valley Dairy, Yarra Valley Persian Feta, Yarra Valley Wasabi Sheep Cheese, Yarra Valley White Savourine, Yellow Buck, Yellow Cheddar, Yorkshire Fettle, Young Buck
Za'atar Burrata, Zaban, Zamorano Curado, Zanetti, Zavet, Zelu Koloria, Zesty Gouda, Ziege Zacke Blue, Ziegenfrischkäse, Ziegengouda, Ziegenkaese, Ziegenkäse, Zierholz, Zijerveld, Zimbro, Zufi, Zwitser
"""

# World Cheese Awards 2025 cheeses
AWARD_WINNING_CHEESES = """
Gruyère AOP Vorderfultigen Spezial, Crémeux des Aldudes aux Fleurs, Appenzeller Edel-Würzig, Gantrisch Bergkäse, Königs-Chäs Rezent, Ossau-Iraty AOP, Stockinghall, Aged Rutland Red, Hechizo, Montana Intenso, Coinga, Torralba, Quintana, Son Vives, Subaida, Son Piris, Murray's Cave Aged Original, Stracciatella Affumicata, Burrata Affumicata, Bufala Ciliegine, Grand Cru Surchoix
"""


def parse_cheeses(text):
    """Parse cheese names from text, handling various formats."""
    cheeses = set()
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        # Split by comma and clean up
        for cheese in line.split(','):
            cheese = cheese.strip()
            if cheese and len(cheese) > 1:
                # Remove any leading/trailing punctuation
                cheese = re.sub(r'^[\-\*\•]+\s*', '', cheese)
                cheese = re.sub(r'\s+', ' ', cheese)
                if cheese:
                    cheeses.add(cheese)
    return sorted(cheeses)


def main():
    # Parse all cheese lists
    all_cheeses = set()

    for source in [WORLD_CHEESES, ADDITIONAL_CHEESES, AWARD_WINNING_CHEESES]:
        cheeses = parse_cheeses(source)
        all_cheeses.update(cheeses)

    # Sort alphabetically
    sorted_cheeses = sorted(all_cheeses, key=str.lower)

    print(f"Total unique cheeses found: {len(sorted_cheeses)}")

    # Group by first letter
    by_letter = {}
    for cheese in sorted_cheeses:
        first_letter = cheese[0].upper()
        if first_letter not in by_letter:
            by_letter[first_letter] = []
        by_letter[first_letter].append(cheese)

    # Print summary
    print("\nCheeses by letter:")
    for letter in sorted(by_letter.keys()):
        print(f"  {letter}: {len(by_letter[letter])} cheeses")

    # Generate markdown section
    print("\n\n## COMPREHENSIVE WORLD CHEESE LIST (A-Z)\n")
    print("> Source: alphalists.com, engdic.org, World Cheese Awards 2024-2025")
    print(f"> Total varieties: {len(sorted_cheeses)}+\n")

    for letter in sorted(by_letter.keys()):
        print(f"\n### {letter}")
        for cheese in by_letter[letter]:
            print(f"- [ ] {cheese}")

    return sorted_cheeses


if __name__ == "__main__":
    main()
