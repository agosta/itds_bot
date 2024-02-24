#!/usr/bin/env python3.10
from random import choice

__author__ = 'Giampaolo Agosta'
__version__= '1.0'
__doc__ = """Generatore casuale di nomi di persona in stile medioevale"""


names = {
 'male' : {
   'Italian'   : [ 'Adamo', 'Adelchi', 'Agnolo', 'Alberto', 'Alfano', 'Amadore', 'Amerigo', 'Andrea', 'Angelo', 'Angiolo', 'Antonio', 'Armando', 'Arrigo', 'Arturo', 'Atenolfo', 'Azzo', 'Baccio', 'Baldo', 'Bartolo', 'Belfante', 'Bello', 'Beneditto', 'Benedetto', 'Beltramo', 'Bernardo', 'Berlinghiero', 'Berto', 'Bindo', 'Biordo', 'Bonanno', 'Boncompagno', 'Alighiero', 'Bonfiglio', 'Bononio', 'Braccio', 'Branca', 'Brancaleone', 'Cacciaguida', 'Calandro', 'Calvo', 'Carlo', 'Francesco', 'Cesare', 'Cherubino', 'Clario', 'Consolato', 'Corrado', 'Cosimo', 'Cristiano', 'Davide', 'Delfino', 'Donato', 'Drudo', 'Egidio', 'Elmo', 'Felice', 'Ferrando', 'Filippo', 'Fioravante', 'Fiore', 'Fortebraccio', 'Franco', 'Galasso', 'Galfrido', 'Gennaio', 'Gentile', 'Gherardo', 'Giacomo', 'Giovanni', 'Giuseppe', 'Goffredo', 'Giusto', 'Grifo', 'Gualdo', 'Gualfredo', 'Guglielmo', 'Guido', 'Guidobaldo', 'Guinibaldo', 'Omobono', 'Gundoaldo', 'Iaquinto', 'Iacomo', 'Inghiramo', 'Jacopo', 'Lamberto', 'Landolfo', 'Lando', 'Lapo', 'Leone', 'Leonardo', 'Lucio', 'Luca', 'Matteo', 'Maffeo', 'Manfredi', 'Marco', 'Marino', 'Marozio', 'Marsilio', 'Tommaso', 'Marzio', 'Michele', 'Bartolomeo', 'Monaldo', 'Napo', 'Napoleone', 'Anastasio', 'Neri', 'Ranieri', 'Oberto', 'Oderigo', 'Oderisi', 'Oliviero', 'Offredo', 'Onesto', 'Orlando', 'Orso', 'Ottobono', 'Pacifico', 'Palmerio', 'Paolo', 'Pasquale', 'Piero', 'Pietro', 'Primo', 'Rambaldo', 'Renato', 'Ridolfo', 'Rinaldo', 'Riccardo', 'Roberto', 'Rodolfo', 'Roffredo', 'Ruggieri', 'Rustico', 'Silvestro', 'Santo', 'Savio', 'Simone', 'Stefano', 'Tancredi', 'Atalarico', 'Tebaldo', 'Tedaldo', 'Tiberio', 'Ubaldo', 'Uberto', 'Ugo', 'Benvenuto', 'Olivieri', 'Vitale', 'Vito', 'Vincenzo' ], 
   'Occitan'   : [ 'Aimers', 'Aimes', 'Alas', 'Albarics', 'Albert', 'Alfans', 'Alias', 'Aliazars', 'Almadric', 'Almavis', 'Amaneus', 'Ancelmes', 'Anfos', 'Arbert', 'Aribert', 'Armans', 'Arnald', 'Arnald', 'Arnaut', 'Azemars', 'Baset', 'Baudois', 'Bausas', 'Berengiers', 'Bernart', 'Bernatz', 'Bertrans', 'Bochartz', 'Centolh', 'Chatbertz', 'Crespi', 'Dalmatz', 'Dalmatz', 'Doat', 'Dorde', 'Dragonetz', 'Drogos', 'Ebratz', 'Enricx', 'Espargs', 'Espas', 'Estaci', 'Esteve', 'Estotz', 'Exuperi', 'Feris', 'Ferrandos', 'Filipot', 'Folcaut', 'Folquets', 'Fortaner', 'Frezols', 'Garcias', 'Gaston', 'Gastos', 'Gaucelis', 'Gaudis', 'Gautiers', 'Gerald', 'Gili', 'Girautz', 'Girvaitz', 'Godafres', 'Gualhartz', 'Guigo', 'Guilabertz', 'Guilhelms', 'Guion', 'Guios', 'Guiotz', 'Guis', 'Imbert', 'Isoartz', 'Izarns', 'Izarts', 'Jaques', 'Jaufres', 'Jehan', 'Joan', 'Joans', 'Johanet', 'Johans', 'Jordan', 'Jordas', 'Joris', 'Karles', 'Lamberts', 'Lops', 'Lozoic', 'Lucatz', 'Marius', 'Martis', 'Michels', 'Miquel', 'Otes', 'Otz', 'Peire', 'Peires', 'Pelfort', 'Perrin', 'Peyre', 'Pons', 'Rainiers', 'Ramonet', 'Ramons', 'Raolf', 'Ratiers', 'Raymon', 'Reiambalts', 'Ricals', 'Ricartz', 'Robertz', 'Rogers', 'Rostans', 'Rotlans', 'Sanc', 'Sancho', 'Savarics', 'Segui', 'Sevis', 'Sicart', 'Simos', 'Tibaut', 'Ucs', 'Ugos', 'Ugs', 'Vezias' ], 
   'French'    : [ 'Adam', 'Aimon', 'Alenard', 'André', 'Anseau', 'Aubert', 'Artaut', 'Aubry', 'Aimery', 'Alberic', 'Alcher', 'Auger', 'Aymer', 'Enguerran', 'Estienne', 'Garnier', 'Geoffroi', 'Gidie', 'Gosse', 'Jehan', 'Josse', 'Onfroi', 'Pierre', 'Roland', 'Artur', 'Alain', 'Aymon', 'Baudoin', 'Benedeit', 'Bernart', 'Charles', 'Charlon', 'Christian', 'Ewart', 'Franceis', 'Leonard', 'Loeis', 'Lohier', 'Marc', 'Martin', 'Michiel', 'Oliver', 'Osmont', 'Peire', 'Perceval', 'Phelipe', 'Pol', 'Raol', 'Reinald', 'Richart', 'Galtier', 'Gervais', 'Georffroy', 'Gefrei', 'Gerart', 'Giffrei', 'Gilebert', 'Gregoire', 'Gualtier', 'Guillaime', 'Guillame', 'Guion', 'Guiot', 'Henri', 'Heraut', 'Herbert', 'Hubert', 'Hugon', 'Jasque', 'Robert', 'Rolant', 'Rollant', 'Sanson', 'Thiebaut', 'Tierri', 'Tristan', 'Tumas', 'Yvain', 'Willeme', 'Raymond', 'Roger', 'Roland', 'Thomas', 'Orthon', 'Marcel', 'Hugues', 'Guillot', 'Olivier', 'Tancred', 'Regnault', 'Jaques', 'Jean', 'Josselin', 'Frédéric', 'Foucaud', 'Erard', 'Evrard', 'Fiebras', 'Gobert', 'Maurice', 'Naimes', 'Nicolas', 'Perrin', 'Philippe', 'Renouart', 'François', 'Etienne', 'Dreux', 'Durand', 'Didier', 'Hervé', 'Josserand', 'Louis', 'Mathieu', 'Martin', 'Denis' ], 
   'Catalan'   : ['Joan', 'Gausfred', 'Girard', 'Guilhem', 'Guillem', 'Ermengol', 'Huguet', 'Ramon', 'Arnau', 'Bernat', 'Berenguer', 'Guifré', 'Rampó', 'Aleran', 'Odalric', 'Humfrid', 'Berà', 'Pere', 'Alfons', 'Jaume', 'Martí', 'Ferran', 'Enric', 'Renat', 'Carles', 'Felip', 'Lluís', 'Andreu', 'Francesc', 'Domingo', 'Bartomeu', 'Mossèn', 'Antoni', 'Gabriel', 'Llucià', 'Miquel', 'Marc', 'Hug', 'Nicolau', 'Cosme', 'Tomàs', 'Jordi', 'Narcís', 'Ot', 'Ponç', 'Guerau', 'Frederic', 'Amanieu', 'Jofre', 'Gilabert', 'Llorenç', 'Nadal', 'Cristofol','Baltasar', 'Dionís', 'Agustí', 'Valentí', 'Jaubert', 'Gregori', 'Pero', 'Vicenç', 'Jeroni', 'Hipòlit', 'Sebastià', 'Dalmau', 'Domènec', 'Nazari', 'Eimeric', 'Miró', 'Vidal', 'Romeu', 'Josep', 'Marí', 'Benet', 'Sanç', 'Pau', 'Didac', 'Pròsper', 'Maurici', 'Onofre', 'Amat', 'Arbert', 'Calvet', 'Dalmu', 'Olivar', 'Perpinyà', 'Guerau', 'Dolcet'], 
   'Spanish'   : ['Juan', 'Pedro', 'Alfonso', 'Gaston', 'Diego', 'Giraldo', 'Rodrigo', 'Martin', 'Hugo', 'Jimeno', 'Inigo', 'Ladron', 'Gonzalo', 'Manrique', 'Tello', 'Bermudo', 'Fernando', 'Ramon', 'Osorio', 'Mendo', 'Ponce', 'Lope', 'Sancho', 'Garcia', 'Fortun', 'Alvaro', 'Gome', 'Gutierre', 'Vela', 'Fernan', 'Ruy', 'Andres', 'Gil', 'Nuno', 'Miguel', 'Pablo', 'Ordono', 'Simon', 'Tomas', 'Francisco', 'Bernardino', 'Antonio', 'Calixto', 'Alonso', 'Guillermo', 'Jaime', 'Enrique', 'Alberto', 'Luis', 'Pascual', 'Jeronimo', 'Baltasar' ], 
   'Portuguese': ['Joao', 'Manuel', 'Afonso', 'Pedro', 'Lourenço', 'Egidio', 'Atao', 'Gonçalo', 'Mendo', 'Teotonio', 'Vasco', 'Alvaro', 'Gomes', 'Diogo', 'Lopo', 'Sancho', 'Martim', 'Gil', 'Estevao', 'Nuno', 'Fernando', 'Mem', 'Antao', 'Martinho', 'Bernardo', 'Sebastiao', 'José', 'Fernao', 'Frederico', 'Damiano', 'Rodrigo', 'Duarte', 'Luis', 'Francisco', 'Vicente', 'Grao', 'Antonio', 'Gregorio', 'Gaspar', 'Garcia', 'Domingo', 'Cristovao', 'Carlos', 'Jorge', 'Egas' ], 
   'Basque'    : ['Antso', 'Aznar', 'Arnaut', 'Gartzi', 'Lupo', 'Azeari', 'Gilen', 'Xemen', 'Bernat', 'Guilen', 'Jon', 'Joxe', 'Bernart', 'Joanes', 'Zuri', 'Ximun', 'Urki', 'Urre', 'Aitor', 'Ander', 'Arnas', 'Andoni', 'Jule', 'Benat', 'Beti', 'Bikendi', 'Bittor', 'Domeka', 'Dunixi', 'Eder', 'Edur', 'Eguzki', 'Ekain', 'Endika', 'Erramun', 'Estebe', 'Gaizka', 'Giro', 'Gorka', 'Haritz', 'Herensuge', 'Inaki', 'Iturri', 'Ion', 'Ineko', 'Joseba', 'Josepe', 'Kemen', 'Koldo', 'Laurendi', 'Ler', 'Lizar', 'Markel', 'Matxin', 'Mikel', 'Mitxel', 'Marz', 'Nikola', 'Pantzeska', 'Patxi', 'Peio', 'Peli', 'Petri', 'Xalbator', 'Urki', 'Unai', 'Urre', 'Zilar', 'Txomin' ], 
   'German'    : ['Cuno', 'Albrecht', 'Andreas', 'Adelman', 'Adam', 'Olbrecht', 'Enderlin', 'Anselm', 'Arnold', 'Arnulf', 'Baldewin', 'Balthasar', 'Bartel', 'Benusch', 'Berchtold', 'Bertold', 'Bernhard', 'Bernt', 'Berold', 'Bertolf', 'Bertram', 'Bruno', 'Burghard', 'Burchard', 'Burgolt', 'Caspar', 'Christoff', 'Clement', 'Conrad', 'Cunrad', 'Cuncze', 'Dietmar', 'Tyme', 'Diterich', 'Ticze', 'Tilo', 'Ditwin', 'Eberhard', 'Eberlin', 'Eckehard', 'Eckel', 'Egidius', 'Elger', 'Engelbrecht', 'Erasmus', 'Asman', 'Fabian', 'Francze', 'Friderich', 'Fredeman', 'Fricz', 'Fridel', 'Gabriel', 'Gebhard', 'Georg', 'Jurge', 'Gerhard', 'Gerlach', 'Gerung', 'Giselbrecht', 'Gyselher', 'Gotbold', 'Gotfrid', 'Gotthard', 'Gregor', 'Greimolt', 'Gumprecht', 'Gunther', 'Hartlib', 'Hartnid', 'Hartmund', 'Heidenrich', 'Heinrich', 'Heynrich', 'Heinz', 'Henke', 'Helwig', 'Hellenbold', 'Hellenbrecht', 'Hempel', 'Herbord', 'Herdegen', 'Herwig', 'Hieronymus', 'Hildebrand', 'Hildiger', 'Hugo', 'Jacob', 'Jekel', 'Johannes', 'Hannus', 'Jost', 'Hensel', 'Hentschel', 'Hans', 'Hannos', 'Lamprecht', 'Lehenhard', 'Leupold', 'Leuthold', 'Libing', 'Ludolf', 'Ludwig', 'Luther', 'Lukas', 'Manegold', 'Marcus', 'Martin', 'Markward', 'Matern', 'Mathias', 'Mathis', 'Meinhard', 'Melchior', 'Michael', 'Neidhart', 'Nicolaus', 'Niclas', 'Niclos', 'Ortlieb', 'Ortolf', 'Otto', 'Otmar', 'Oswald', 'Pankratz', 'Partschfall', 'Paschalis', 'Paul', 'Peter', 'Procop', 'Reinhard', 'Reiprecht', 'Reynfrid', 'Richart', 'Richolf', 'Richel', 'Rudeger', 'Rudel', 'Rudolf', 'Rumpolt', 'Ruprecht', 'Sigeberht', 'Sigfrid', 'Sighard', 'Sigmund', 'Steffan', 'Symon', 'Thomas', 'Ulrich', 'Valten', 'Volkmar', 'Walther', 'Warmund', 'Wigand', 'Wikman', 'Wilrich', 'Wilhelm', 'Winand', 'Winrich', 'Wolf', 'Wiprecht', 'Wolfgang', 'Zacharias' ], 
   'English'   : ['William', 'Robert', 'John', 'Walter', 'Hugh', 'Henry','Richard', 'Ralph', 'Thomas', 'Roger', 'Adam', 'Alphonse', 'Alexander', 'Albert', 'Aldred', 'Alan', 'Aglovale', 'Arnold', 'Arthur', 'Bartholomew', 'Bardolph', 'Barnabas', 'Basil', 'Baudwin', 'Bennet', 'Bernard', 'Bliant', 'Blaise', 'Bryce', 'Castor', 'Charles', 'Cerdic', 'Cyr', 'Daniel', 'David', 'Denis', 'Dinadan', 'Diggory', 'Drogo', 'Edwin', 'Elias', 'Eliot', 'Eluard', 'Eustace', 'Everard', 'Faramond', 'Frederick', 'Fulke', 'Gabriel', 'Galleron', 'Gareth', 'Geoffrey', 'George', 'Gerald', 'Gerard', 'Gervase', 'Gilbert', 'Giles', 'Godwin', 'Gregory', 'Griffith', 'Griffen', 'Gunther', 'Guy', 'Hamond', 'Hardwin', 'Hector', 'Herbert', 'Herman', 'Hildebrand', 'Hubert', 'Humphrey', 'Isaac', 'Ingram', 'Isenbard', 'Ives', 'James', 'Jasper', 'Jeremy', 'Jocelyn', 'Jordan', 'Joseph', 'Lambert', 'Laurence', 'Leofwin', 'Lionel', 'Lucan', 'Lucius', 'Luke', 'Mabon', 'Manfred', 'Maynard', 'Mark', 'Martin', 'Matthew', 'Merek', 'Michael', 'Milo', 'Miles', 'Nicholas', 'Nigel', 'Noah', 'Osric', 'Ogier', 'Paul', 'Percival', 'Peter', 'Philip', 'Piers', 'Randel', 'Ranulph', 'Reginald', 'Rowan', 'Sampson', 'Salomon', 'Theobald', 'Thurstan', 'Tristram', 'Turstin', 'Ulric', 'Urian', 'Wolfstan', 'Warner', 'Wymond', 'Warin'], 
   'Hungarian' : ['Almos', 'Ampud', 'Apa', 'Atyusz', 'Orbasz', 'Bank', 'Kalan', 'Korlat', 'Brocca', 'Bela', 'Bucan', 'Chama', 'Coloman', 'Charena', 'Ugrin', 'Vejte', 'Ded', 'Denes', 'Elvin', 'Imre', 'Francica', 'Fonsol', 'Farkas', 'Cronik', 'Eth', 'Gereon', 'Geza', 'Csepan', 'Alexander', 'Pat', 'Saul', 'Buzad', 'Hahold', 'Hartvik', 'Lampert', 'Mika','Uros', 'Simon', 'Boris', 'Kokenyes', 'Bulcsu', 'Laszlo', 'Makar', 'Mika', 'Mikod', 'Mog', 'Moch', 'Majos', 'Mojs', 'Nana', 'Micklos', 'Tore', 'Leustach', 'Rednald', 'Smaragd', 'Istvan', 'Jakab', 'Kemeny', 'Lorinc', 'Henrik', 'Gyula', 'Andras', 'Todor', 'Mate', 'Peter', 'Mark', 'Ivanka', 'Ivahon', 'Gergely', 'Tamas', 'Makarias', 'Tiba', 'Vata', 'Vilcina', 'Marcell', 'Marton', 'Valter', 'Gyarfas', 'Ivachin', 'Lukacs', 'Dezso', 'Domokos', 'Domonkos', 'Gyorgy', 'Job', 'Egyed', 'Tiborc', 'Janos', 'Boleszlo' ], 
   'Romanian'  : ['Ioan', 'Petru', 'Stefan', 'Bodgan', 'Latcu', 'Alexandru', 'Roman', 'Ilie', 'Nicolae', 'Antonie', 'Miron', 'Alecu', 'Anton', 'Gheorghe', 'Constantin', 'Emanoil', 'Mihail', 'Florian', 'Ieremia', 'Dinu', 'Costache', 'Radu', 'Nicu', 'Iancu', 'Gavril', 'Dimitrie', 'Iana', 'Ion', 'Grigore', 'Dumitru', 'Paul', 'Pintea', 'Aurel', 'Iuga', 'Grigore', 'Barbu', 'Ciubar', 'Aristide', 'Serban', 'Victor', 'Dan', 'Iosif', 'Vlad', 'Vladislav', 'Leon', 'Manole', 'Iane', 'Toma', 'Mircea', 'Iancu', 'Horia', 'Andrei', 'Liviu', 'Mihai', 'Marian', 'Sorin', 'Virgil', 'Zaharia', 'Ovidiu', 'Victor', 'Iuliu', 'Traian', 'Rasvan'], 
   'Slavonic'  : ['Adam', 'Aleksandr', 'Chestislav', 'Daniil', 'David', 'Filipp', 'Gavriil', 'Grigorii', 'Iakov', 'Ilia', 'Iosif', 'Luka', 'Isaak', 'Matthia', 'Mikhail', 'Samuil', 'Simon', 'Stefan', 'Vasilii', 'Zacharia', 'Varnava', 'Timothei', 'Thoma', 'Petr', 'Avraam', 'Andrei', 'Boris', 'Borislav', 'Vladimir', 'Stanislav', 'Svorad', 'Vladislav', 'Casimir', 'Radim', 'Milos', 'Lubo', 'Goran', 'Slava', 'Vuk', 'Vlada', 'Dusan', 'Zivan', 'Gleb', 'Igor', 'Dimitri', 'Yaroslav', 'Afanasiy', 'Ivan', 'Nikolai', 'Mikula', 'Zhizomir', 'Grigori', 'Bojan', 'Vsevold', 'Mstislav', 'Milutin', 'Antoniy', 'Sviatopolk', 'Iziaslav', 'Sviatoslav', 'Ostromir', 'Konstantin', 'Theodosiy', 'Ioakim', 'Iakov', 'Moisei', 'Varlaam', 'Dobromir', 'Theodor', 'Aldimir', 'Rostislav', 'Vissarion', 'Kosmas', 'Ignatii', 'Hranislav', 'Prodan', 'Mladen', 'Plamen', 'Lech', 'Ognjen', 'Bogdan', 'Bohumil', 'Borislav', 'Zelimir', 'Budimir', 'Bratislav', 'Dalibor', 'Lutobor', 'Strogobor', 'Falibor', 'Havlimir', 'Techomir', 'Tesimir', 'Castimir', 'Ceslav', 'Bozidar', 'Dobromir', 'Dobrogost', 'Dobromil', 'Dragomir', 'Domagoj', 'Domabor', 'Godemir', 'Radogost', 'Hostirad', 'Hviezdoslav', 'Godzimir', 'Jaropolk', 'Kazimir', 'Jaromir', 'Ludovit', 'Lutoslav', 'Lubor', 'Lutomir', 'Kresivoje', 'Vlastimil', 'Milomir', 'Miloslav', 'Mirogod', 'Damir', 'Vitomir', 'Krasimir', 'Rastimir', 'Branimir', 'Mislav', 'Mstivoje', 'Ratibor', 'Ratimir', 'Racimir', 'Stanimir', 'Stanislav', 'Svetoslav', 'Svetozar', 'Svetobor', 'Velimir', 'Ladislav', 'Vlastimir', 'Zdeslav', 'Zlatibor', 'Zlatan', 'Lev'], 
   'Gaelic'    : ['Conchobor', 'Mael Isa', 'Maelcoluim', 'Aed', 'Gillagori', 'Gillabhrenainn', 'Lurint', 'Amhlaoibh', 'Fer Domnach', 'Giolla Domhnaill', 'Torquil', 'Dubh Chobhlaigh', 'Domhnall', 'Fiannchad', 'Ragnall', 'Amhlaeibh', 'Muireadhach', 'Brian', 'Muirceartach', 'Aedh Dall', 'Cathal', 'Donnell', 'Murtogh', 'Mathghamhain', 'Samhradhan', 'Melaghlin', 'Aodh', 'Donnchadh', 'Domnall', 'Brodar', 'Muirgius', 'Ruairi', 'Diarmait', 'Gilla Mo Choinni', 'Murrogh', 'Muirgheas', 'Donn Sleibhe', 'Gilla Cheallaigh', 'Uada', 'Teige', 'Tadhg', 'Enna', 'Tomaltach', 'Mael Sechlainn', 'Cormac', 'Cu Coirne', 'Madudan' ],
   'Norse'     : [ 'Arne', 'Birger', 'Bjoern', 'Bo', 'Erik', 'Frode', 'Gorm', 'Halfdan', 'Harald', 'Knud', 'Kare', 'Leif', 'Njal', 'Roar', 'Rune', 'Sten', 'Skarde', 'Sune', 'Troels', 'Toke', 'Torsten', 'Trygve', 'Ulf', 'Oedger', 'Age', 'Agmundr', 'Agnarr', 'Aki', 'Aleifr', 'Alfarr', 'Alfrikr', 'Alfvin', 'Alfgautr', 'Anundr', 'Ari', 'Arnfinnr', 'Asbjorn', 'Arnvidr', 'Asgeirr', 'Arnthorr', 'Asmundr', 'Adhalsteinn', 'Asvaldr', 'Bjarni', 'Bjartr', 'Bardhr', 'Baggi', 'Audhun', 'Brandr', 'Brodhir', 'Dagr', 'Dagfinnr', 'Eirikr', 'Erlendr', 'Eindridhi', 'Einarr', 'Egill', 'Eileifr', 'Eysteinn', 'Erlingr', 'Eyvindr', 'Finnr', 'Felagi', 'Flaemingr', 'Frodhi', 'Gauti', 'Gautstafr', 'Geirmundr', 'Geirr', 'Gunnarr', 'Gulbrandhr', 'Gunni', 'Gunnvaldr', 'Gudhbrandhr', 'Gudhfrodhr', 'Gudhini', 'Gudhleifr', 'Gudhmundr', 'Hakon', 'Halfdan', 'Hallbjorn', 'Gudhrodhr', 'Hallsteinn', 'Hallthor', 'Hallvardhr', 'Hamundr', 'Helgi', 'Hjalmarr', 'Hildingr', 'Hemingr', 'Holmgeirr', 'Hrafn', 'Hreidharr', 'Hroarr', 'Hroaldr', 'Hrodhgeirr', 'Hrodhulfr', 'Hugleikr', 'Ingi', 'Ivarr', 'Josteinn', 'Karl', 'Ketill', 'Knutr', 'Kori', 'Magni', 'Mundi', 'Oddr', 'Oddvar', 'Ottar', 'Ragnarr', 'Olvir', 'Ragnvaldr', 'Radhulfr', 'Runi', 'Sigfrodhr', 'Sigmundr', 'Sigsteinn', 'Stali', 'Snorri', 'Sindri', 'Steingrimmr', 'Stigandr', 'Sumarlidhi', 'Sverrir', 'Sveinn', 'Thorarinn', 'Thorbjorn', 'Thorfredhr', 'Thorgeirr', 'Thorgnyr', 'Thorir', 'Thorgisl', 'Thorleikr', 'Thormondr', 'Thorsteinn', 'Thorvaldr', 'Throndr', 'Valdimarr', 'Uni', 'Ulfr', 'Tryggvi', 'Toki', 'Tofi', 'Valthjofr', 'Vegardhr', 'Vetrlidhi', 'Vebjorn', 'Vigi', 'Vragi', 'Yngvarr' ],   
   'Arabic'      : ['Umara', 'Usama', 'Muhammad', 'Yaqut', 'Hammad', 'Bassam', 'Bashrun', 'Badi', 'Ibrahim', 'Ishaq', 'Mubarak', 'Ahmad', 'Diya', 'Amin', 'Zakariyya', 'Muhadhdhab', 'Ali', 'Majd', 'Murshid', 'Mansur', 'Muhyi', 'Hassan', 'Uthman', 'Abd ar-Rahman', 'Abd Allah', 'Abd al-Jabbar', 'Mustafa', 'Sulayman', 'Umar', 'Hamid', 'Izz al-Din', 'Afif al-Din', 'Adlan', 'Farid', 'Sharaf al-Din', 'Salih', 'Jamal', 'Jibril', 'Lisan', 'Tamim', 'Tamam', 'Yahya', 'Hamdan', 'Jafar', 'Urfah', 'Habib'],
   'Latin'     : [ 'Anicius', 'Antonius', 'Agrippa', 'Appius', 'Caesar', 'Cornelius', 'Calpurnius', 'Claudius', 'Decimus', 'Darius', 'Decius', 'Faustus', 'Gaius', 'Baldus', 'Benedictus', 'Clarius', 'Egidius', 'Felix', 'Ianuarius', 'Homobonus', 'Marsilius', 'Marotius', 'Boetius', 'Marcus', 'Marinus', 'Nero', 'Tiberius', 'Lucius', 'Vitalis', 'Vincens', 'Victor', 'Paciferus', 'Petrus', 'Savius', 'Servius', 'Tullius', 'Marcius', 'Quintus', 'Quintilius', 'Ursus', 'Leo', 'Iustus', 'Primus', 'Secundus', 'Quartus', 'Sextus', 'Pompeius', 'Iulius', 'Aurelius', 'Ambrosius', 'Flavius', 'Domitius', 'Titus', 'Titianus', 'Aurelianus', 'Marcianus', 'Quintilianus', 'Emilianus', 'Scipio', 'Cornelianus', 'Iulianus', 'Domitianus', 'Octavius', 'Augustus', 'Pompilius', 'Aelius', 'Bonifacius', 'Honorius', 'Sergius', 'Magnus', 'Mercutius', 'Polonius', 'Decianus', 'Servianus', 'Servilius', 'Severus', 'Antoninus', 'Aetius', 'Petrus', 'Iohannes', 'Guillelmus', 'Albertus', 'Henricus', 'Iacobus', 'Gerardus', 'Martinus', 'Bernardus', 'Candidus', 'Robertus', 'Vincentius', 'Thomas', 'Paulus', 'Rogerius', 'Arnulfus', 'Hugo', 'Odo', 'Isidorus', 'Landulfus', 'Baldericus', 'Anselmus' ],
   'Greek'     : ['Demetrios', 'Euthymios', 'Eusebius', 'Michael', 'Athanasios', 'Andronikos', 'Leontios', 'Ioannis', 'Nicholas', 'Photios', 'Eustathios', 'Leon', 'Gregorios', 'Georgios', 'Theodoros', 'Alexios', 'Cassianos', 'Konstantinos', 'Basileios', 'Nikephoros', 'Epiphanios', 'Adrianos', 'Alexander', 'Ammonios', 'Anthemios', 'Apasios', 'Arcadios', 'Bardas', 'Belisarios', 'Christodoulos', 'Konstas', 'Kosmas', 'Cyrillos', 'Damianos', 'Demetrios', 'Gennadios', 'Genesios', 'Maniakes', 'Isidoros', 'Isaakios', 'Kostas', 'Loukas', 'Longinos', 'Manouel', 'Markos', 'Maurikios', 'Petros', 'Savvas', 'Niketas', 'Symeon', 'Theoleptos', 'Zacharias', 'Theophylaktos', 'Theophanis', 'Theophilos' ],
   'Hebrew'    : ['Baruch', 'Aaron', 'Abraham', 'Ayyub', 'David', 'Isaac', 'Jacob', 'Jedaiah', 'Joseph', 'Mordochee', 'Samuel', 'Nathan', 'Moses', 'Avigdor', 'Asser', 'Israel', 'Phineas', 'Salomon', 'Simon', 'Ithiel', 'Obadiah', 'Meshullam', 'Joab', 'Meir', 'Samson', 'Hushiel', 'Efrayim'], 
   'Welsh' : ['Madoc', 'Deykin', 'Eynon', 'Iorwerth', 'Iarword', 'Adam', 'Ieuan', 'Gronw', 'Groneu', 'Ithel', 'Gwyn', 'Gwin', 'Kenuric', 'Kenneric', 'Cadugan', 'Ryryd', 'Reryd', 'Tegwaret', 'Meiler', 'Meyler', 'Edenevet', 'Gurgeneu', 'Lewelin', 'Lewelyn', 'Gwion', 'Gwyon', 'Howel', 'Tuder', 'Candalo', 'Candalou', 'Madin', 'Madyn', 'Meuric', 'Meuryk', 'Lowarch', 'Gwilim', 'Griffri', 'Gryffry', 'Moridic', 'Morydic', 'Kedivor', 'Yago', 'Iockin', 'Iokyn', 'Res', 'Reys', 'Blethin', 'Blethint', 'Kevenard', 'Mereduth', 'Thomas', 'Ieuaf', 'Morvran', 'Seysild', 'Dehewint', 'Wasdeny', 'Leget', 'Hova', 'Gogan', 'Idnerth', 'Idenerth'],
 },
 'female' : {
   'Italian'   :  [ 'Accorsa', 'Adelasia', 'Agnola', 'Agata', 'Alagia', 'Altabella', 'Alteria', 'Angela', 'Arcangela', 'Angiola', 'Antonia', 'Armilia', 'Artellaide', 'Augustina', 'Aurisma', 'Baccia', 'Balda', 'Bartola', 'Beatrice', 'Bella', 'Beneditta', 'Benedetta', 'Belladonna', 'Bernarda', 'Berlinghiera', 'Berta', 'Bona', 'Bonafemina', 'Bonizzella', 'Boncompagna', 'Bontelda', 'Braccesca', 'Brunisenda', 'Carla', 'Francesca', 'Cherubina', 'Clara', 'Consolata', 'Caterina', 'Cosima', 'Cristiana', 'Clarice', 'Domitilla', 'Donata', 'Delfina', 'Egidia', 'Ermellina', 'Epifania', 'Fillide', 'Fiordalisa', 'Florese', 'Franca', 'Gherarda', 'Giovanna', 'Giuseppa', 'Giusta', 'Gigliola', 'Ginevra', 'Gualdrada', 'Grimelda', 'Guglielma', 'Guida', 'Guinelda', 'Gundoalda', 'Iaquinta', 'Imelda', 'Inghilesca', 'Isabella', 'Jacobella', 'Landa', 'Leonetta', 'Leonora', 'Lucia', 'Eleonora', 'Elisabetta', 'Liutgarda', 'Lucrezia', 'Lottiera', 'Marina', 'Marozia', 'Marsilia', 'Maddalena', 'Marzia', 'Michela', 'Margherita', 'Maralda', 'Matilde', 'Nera', 'Anastasia', 'Nencia', 'Nina', 'Oberta', 'Obbedienza', 'Onesta', 'Orsa', 'Ottabona', 'Pacifica', 'Palmeria', 'Paola', 'Pasqua', 'Piera', 'Pace', 'Pandolfa', 'Pentesilea', 'Renata', 'Piccarda', 'Pazienza', 'Apollonia', 'Roberta', 'Prassede', 'Prudenzia', 'Polissena', 'Richilde', 'Rosa', 'Santa', 'Savia', 'Sapienza', 'Stefania', 'Esmeralda', 'Teodesia', 'Tebalda', 'Tedalda', 'Tiberia', 'Ubaldesca', 'Uberta', 'Uga', 'Benvenuta', 'Veniera', 'Verde', 'Veridiana', 'Zelante' ],  
   'Occitan'   : [ 'Alienor', 'Alazais', 'Anais', 'Girauda', 'Mireio', 'Garsenda', 'Aicelina', 'Alice', 'Andreva', 'Audiarda', 'Austorga', 'Baussana', 'Bonassia', 'Blanca', 'Constansa', 'Elionor', 'Ermengarda', 'Ermessenda', 'Esquiva', 'Galiana', 'Elena', 'Petrona', 'Rixenda', 'Rubea', 'Sancha', 'Willelma', 'Agnessona', 'Anthonye', 'Aymoneta', 'Audisia', 'Catherina', 'Fina', 'Francesia', 'Guia', 'Henrieta', 'Ysabella', 'Losaneta', 'Sibilia', 'Yzabeau', 'Suzanne', 'Margarette', 'Laurensa', 'Johanna', 'Janseranda', 'Jacquelyna', 'Guirauda', 'Clareta', 'Bernarda', 'Bertranda', 'Anne', 'Loise', 'Lisette', 'Jammeta', 'Marta', 'Ramonda', 'Tuffayna', 'Pieret', 'Peyrinne', 'Olyna', 'Mondette', 'Nonela', 'Ysabel', 'Alayda', 'Gualharda', 'Bertrana', 'Giralda', 'Assalhida', 'Assenda', 'Petrona', 'Claremonda', 'Gazenda', 'Tanzeda', 'Pelegrina', 'Bona', 'Mabila' ], 
   'French'    : ['Adela', 'Aenor', 'Agnes', 'Alice', 'Azalais', 'Mathilde', 'Avoise', 'Mahaut', 'Melisende', 'Jehanne', 'Cecile', 'Cunstance', 'Ele', 'Gunnor', 'Mahelt', 'Marie', 'Marion', 'Nicolete', 'Ysabel', 'Adeline', 'Agnesot', 'Ameline', 'Amelot', 'Anne', 'Aude', 'Blanche', 'Catherine', 'Chrestienne', 'Clarisse', 'Collette', 'Denise', 'Denisette', 'Dorian', 'Edine', 'Emmelot', 'Florence', 'Guillette', 'Guillemette', 'Genevote', 'Gervaise', 'Guoite', 'Honnorée', 'Ide', 'Jaqueline', 'Loyse', 'Jaquette', 'Jehanne', 'Jehannette', 'Joie', 'Juliote', 'Lutisse', 'Mahault', 'Margot', 'Marguerite', 'Mesot', 'Mirabelle', 'Nicole', 'Martine', 'Mesot', 'Pasquette', 'Perrette', 'Perotte', 'Oudine', 'Typhannie', 'Sybille', 'Symonne', 'Serena' ], 
   'Catalan'   : ['Maria', 'Violant', 'Isabel', 'Agnès', 'Arsenda', 'Margarida', 'Elisenda', 'Elionor', 'Elisabet', 'Joana', 'Ingilrada', 'Guillema', 'Francesca', 'Caterina', 'Berenguera', 'Gudinilda', 'Blanca', 'Constança', 'Ramona', 'Sança', 'Saurina', 'Saurimonda', 'Teresa', 'Amèlia', 'Esclarmonda', 'Manuela', 'Celeriana', 'Aurucia', 'Llorença', 'Sotera', 'Magdalena', 'Angela', 'Arsendis', 'Ermessendis', 'Titbores', 'Valencia', 'Ermessen'], 
   'Spanish'   : ['Maria', 'Florencia', 'Teresa', 'Elvira', 'Estefania', 'Ximena', 'Blanca', 'Inés', 'Leonor', 'Urraca', 'Petronila', 'Sancha', 'Talesa', 'Mafalda', 'Dulce', 'Constanza', 'Gontrodo', 'Jimena', 'Teresa', 'Beatriz', 'Aldonza', 'Isabel', 'Berenguela', 'Violante', 'Juana', 'Mencia', 'Margarita', 'Cecilia', 'Bonanada', 'Angela', 'Lucrecia', 'Catalina', 'Toda', 'Oria', 'Riquilda', 'Cristina', 'Casilda', 'Ermensinda', 'Palla', 'Velasquita'], 
   'Portuguese': ['Maria', 'Beatriz', 'Branca', 'Gudilona', 'Guoimar', 'Ilduara', 'Ines', 'Isabel', 'Matilde', 'Mafalda', 'Luisa', 'Sancha', 'Mecia', 'Teresa', 'Urraca', 'Vataça', 'Leonor', 'Elvira', 'Enderquina', 'Filipa', 'Catarina', 'Constança', 'Dulce', 'Joana', 'Violante', 'Mumadona', 'Ana', 'Brites'], 
   'Basque'    : ['Arantxa', 'Aintza', 'Amets', 'Arine', 'Arrats', 'Arrosa', 'Edurne', 'Bittori', 'Estebeni', 'Egutzkine', 'Erregina', 'Gartzene', 'Florentxi', 'Gorria', 'Gotzone', 'Gurutze', 'Igone', 'Iturrieta', 'Jone', 'Josebe', 'Joxepa', 'Julene', 'Kemena', 'Lide', 'Luixa', 'Maritxu', 'Nerea', 'Matxalen', 'Mendiete', 'Mikele', 'Pantxike', 'Pauli', 'Urdina', 'Urkia', 'Ximena', 'Xixili', 'Zurine'], 
   'German'    : ['Agathe', 'Agnise', 'Aleyd', 'Amalie', 'Anna', 'Berchte', 'Beate', 'Clare', 'Elisabeth', 'Demut', 'Enede', 'Engel', 'Eufemia', 'Gerdrut', 'Gerusch', 'Hedwig', 'Helena', 'Hildegund', 'Irmeltrud', 'Isentrud', 'Jutte', 'Katherine', 'Kungunde', 'Liphilt', 'Lucie', 'Magdalena', 'Margarethe', 'Marusch', 'Marie', 'Mechthild', 'Osterhild', 'Ottilie', 'Sophie', 'Ursula', 'Yrmengard', 'Veronica', 'Sanne', 'Cecilia', 'Christine'], 
   'English'   : ['Alice', 'Matilda', 'Agnes', 'Joan', 'Isabella', 'Emma', 'Margaret', 'Beatrice', 'Mabel', 'Cecilia', 'Adelina', 'Alma', 'Althea', 'Acelina', 'Anais', 'Aldith', 'Alyson', 'Amicia', 'Amelina', 'Anne', 'Artemisia', 'Athelina', 'Audry', 'Augusta', 'Berta', 'Blanche', 'Brangwine', 'Bridget', 'Cassandra', 'Cateline', 'Caterina', 'Cecily', 'Celestria', 'Constance', 'Clare', 'Clarice', 'Christina', 'Dameta', 'Delia', 'Edeva', 'Edith', 'Eglenti', 'Elle', 'Elaine', 'Eleanor', 'Eva', 'Elizabeth', 'Elysande', 'Emily', 'Emeline', 'Evaine', 'Evelune', 'Felicia', 'Florence', 'Floria', 'Genevieve', 'Gisela', 'Gracia', 'Gratia', 'Guinevere', 'Gundred','Gwendolen', 'Helewise','Ida', 'Ingerith', 'Isemay', 'Isolde', 'Ivette', 'Johanna', 'Joyce', 'Joya', 'Juliana', 'Laudine', 'Lavena', 'Leticia', 'Legarda', 'Lia', 'Lillian', 'Lena', 'Lunete', 'Magdalen', 'Margery', 'Mary', 'Molly', 'Martha', 'Marie', 'Maria', 'Marion', 'Marian', 'Maud', 'Maude', 'Miriel', 'Milicent', 'Odelina', 'Orella', 'Regina', 'Ricolda', 'Roana', 'Rosa', 'Rosamund', 'Sarah', 'Sela', 'Sigga', 'Susanna' ,'Swanhild', 'Theda', 'Thora', 'Venetia', 'Viviane', 'Ysmeine' ], 
   'Hungarian' : ['Erzsebet', 'Katalin', 'Maria', 'Richeza', 'Felicia', 'Anasztazia', 'Gizella', 'Judit', 'Jolan', 'Eufemia', 'Agafia', 'Krisztina', 'Adelhaid', 'Ilona', 'Eufrozina', 'Agnes', 'Anna', 'Margit', 'Konstancia', 'Gertrud', 'Beatrix', 'Izabella', 'Fennena', 'Viola', 'Zsofia', 'Odola', 'Teodora', 'Piroska', 'Iren'], 
   'Romanian'  : ['Ioana', 'Nadeja', 'Elisa', 'Stefana', 'Maria', 'Anastasia', 'Natalia', 'Ruxandra', 'Casandra', 'Elena', 'Ecaterina', 'Musata', 'Margareta', 'Aliona', 'Catalina', 'Iulia', 'Ileana', 'Marina', 'Sorana', 'Lucia', 'Roxana', 'Mariana', 'Magda', 'Angela', 'Daniela', 'Otilia', 'Stefania', 'Tatiana', 'Mihaela', 'Mirela', 'Oana', 'Antoaneta', 'Laura', 'Anca', 'Irina', 'Adina', 'Stela', 'Anisoara', 'Petronela'], 
   'Slavonic'  : ['Anna', 'Maria', 'Xenia', 'Elisabeti', 'Esthir', 'Eva', 'Iudith', 'Lydia', 'Magdalina', 'Ruth', 'Susanna', 'Ludmila', 'Nadezhda', 'Zdislava', 'Jagoda', 'Dusa', 'Vesna', 'Slava', 'Jasna', 'Ljuba', 'Nada', 'Mila', 'Vera', 'Lada', 'Gavrila', 'Ulita', 'Evgenia', 'Elena', 'Vladmila', 'Zelimira', 'Vladena', 'Slavena', 'Bratomira', 'Stanimira', 'Rostimira', 'Radmila', 'Jarmila', 'Kvetoslava', 'Krasimira', 'Zvedzana', 'Blazena', 'Zora', 'Dobra', 'Snezana', 'Vesela', 'Mira', 'Zlata', 'Svetlana', 'Bogdana', 'Borislava', 'Miloslava', 'Rada', 'Ognjenka', 'Zvonimira'], 
   'Gaelic'    : ['Dubh Essa', 'Aoife', 'Mor', 'Derb Forgaill', 'Dubh Chonlaigh', 'Cacht', 'Gormlaith', 'Mael Muire', 'Slaine', 'Caineach', 'Creassa', 'Dub Lemna', 'Gormflaith', 'Orlaith', 'Saerlaith', 'Sunniva', 'Melkorka', 'Samthann', 'Sarnait', 'Eithne', 'Sodelb', 'Derchairthinn', 'Damhnade', 'Caintigern', 'Conainne', 'Gobnait', 'Tochumra', 'Modwenna'],
   'Norse'     : [ 'Astrid', 'Bodil', 'Frida', 'Gertrud', 'Gro', 'Estrid', 'Hilda', 'Gudrun', 'Gunhild', 'Helga', 'Inga', 'Liv', 'Randi', 'Signe', 'Sigrid', 'Revna', 'Sif', 'Tora', 'Tove', 'Thyra', 'Thurid', 'Yrsa', 'Ulfhild', 'Ase', 'Alfhild', 'Alof', 'Arnbjorg', 'Asa', 'Asdis', 'Ashildr', 'Asta', 'Audhrhildr', 'Bergljot', 'Borghildr', 'Brynhildr', 'Brynia', 'Dagrun', 'Dagny', 'Dagmaer', 'Edda', 'Eydis', 'Eyvor', 'Grimhildr', 'Gulla', 'Gunna', 'Gunnbjorg', 'Gunnhildr', 'Gunnvor', 'Gudhlaug', 'Gudhleif', 'Gyda', 'Gudhrun', 'Hallthora', 'Herleif',  'Hildr', 'Hildigunnr', 'Holmfridhr', 'Hreidhunn', 'Ingibjorg', 'Ingigerdhr', 'Ingridhr', 'Ingvildr', 'Idhunn', 'Jorunnr', 'Katla', 'Magnhildr', 'Myrgjol', 'Oddbjorg', 'Ragna', 'Olaug', 'Oddrun', 'Ragnbjorg', 'Ragnfridhr', 'Ragnheidr', 'Runa', 'Saldis', 'Signy', 'Sigridhr', 'Sigrun', 'Steinunn', 'Svanhildr', 'Thone', 'Thora', 'Thordis', 'Thorbjorg', 'Thorfridhr', 'Thorhildr', 'Thrud', 'Thorveig', 'Thorunn', 'Thorvi', 'Tofa', 'Thyri', 'Unnr', 'Vigdis', 'Yngvildr' ],   
   'Arabic'      : ['Mahd', 'Afira', 'Laila', 'Jalila', 'Safiyah', 'Umama', 'Ishraqa', 'Juhaifa', 'Qutayla', 'Fatima', 'Maisun', 'Humayda', 'Atiqa', 'Amra', 'Dahna', 'Hajna', 'Raabia', 'Ulayya', 'Lubana', 'Inan', 'Zahra', 'Asiya', 'Aaisha', 'Shariyah', 'Fadi', 'Zabba', 'Arib', 'Hafsa', 'Mariam', 'Khadija', 'Taqiyya', 'Safiyya', 'Wallada', 'Qasmuna', 'Muhia', 'Hind', 'Buthaina', 'Zaynab', 'Nazhun' ],
   'Latin'     : [ 'Anicia', 'Antonia', 'Agrippina', 'Appia', 'Pulchra', 'Cornelia', 'Calpurnia', 'Claudia', 'Decima', 'Daria', 'Decia', 'Fausta', 'Gaia', 'Benedicta', 'Claria', 'Egidia', 'Felicia', 'Ianuaria', 'Marsilia', 'Marotia', 'Boetia', 'Marcella', 'Marina', 'Nevia', 'Tiberia', 'Lucia', 'Victoria', 'Pacifera', 'Petra', 'Savia', 'Servia', 'Tullia', 'Marcia', 'Quinta', 'Quintilia', 'Ursa', 'Leonilla', 'Iusta', 'Primus', 'Secunda', 'Quarta', 'Sexta', 'Pompeia', 'Iulia', 'Aurelia', 'Ambrosia', 'Flavia', 'Domitia', 'Titiana', 'Aureliana', 'Marciana', 'Quintiliana', 'Emiliana', 'Corneliana', 'Iuliana', 'Domitiana', 'Octavia', 'Augusta', 'Pompilia', 'Aelia', 'Bonifacia', 'Honoria', 'Sergia', 'Maia', 'Deciana', 'Serviana', 'Servilia', 'Severa', 'Antonina', 'Aetia', 'Domitilla', 'Lucilla' ],
   'Greek'     : ['Eudocia', 'Kassia', 'Anna', 'Aelia', 'Theodora', 'Irene', 'Maria', 'Philippa', 'Helena', 'Barbara', 'Zoe', 'Agatha', 'Theophanu', 'Thecla', 'Theoktiste', 'Anthusa', 'Danielis', 'Euphrosyne', 'Calinichia', 'Sophia', 'Anastasia', 'Prokopia', 'Theodota', 'Euprepia', 'Eulogia', 'Eugenia', 'Ariadne', 'Despoina', 'Melaina', 'Metrodora', 'Olympias', 'Styliane', 'Theophano', 'Theodule', 'Simonis' ],
   'Hebrew'    : [ 'Sarah', 'Rachel', 'Basseva', 'Bella', 'Astruga', 'Bona', 'Cara', 'Cima', 'Clara', 'Elisa', 'Esther', 'Formosa', 'Hadassah', 'Laetitia', 'Luna', 'Margalit', 'Marina', 'Matrona', 'Mazalta', 'Mima', 'Mina', 'Mira', 'Miriam', 'Oro', 'Rebeca', 'Rivkah', 'Pulchra', 'Sol', 'Regina', 'Vita', 'Yerussa', 'Viva', 'Chana', 'Guta' ],  
   'Welsh' : ['Angharat', 'Wentlian', 'Wentliana', 'Wladusa', 'Wladus', 'Lewke', 'Tudgech', 'Dugech', 'Leweke', 'Leuke', 'Eva', 'Tangwistel', 'Generys', 'Generis', 'Wervel', 'Wervela', 'Wervilla', 'Morud', 'Morwid', 'Morwith', 'Nest', 'Hunith', 'Gwen', 'Wledyr', 'Wledir', 'Wladur', 'Morvel','Mevanou', 'Eduduwel', 'Erdiduwol', 'Maderun', 'Gwerith', 'Marured', 'Perweur', 'Genithles', 'Enith', 'Enid', 'Wir', 'Ewerich', 'Mabilia', 'Mary', 'Milisandia', 'Elena'],
 },
}

regions = {
  'Occitania'     : ['Occitan', 'Occitan', 'Occitan', 'Basque', 'Catalan'],
  'France'        : ['French'],
  'Francia'       : ['French'],
  'Italy'         : ['Italian'],
  'Italia'        : ['Italian'],
  'Germany'       : ['German', 'German', 'German', 'German', 'Slavonic'],
  'Germania'      : ['German', 'German', 'German', 'German', 'Slavonic'],
  'Hungary'       : ['Hungarian', 'Romanian', 'Slavonic'],
  'Ungheria'      : ['Hungarian', 'Romanian', 'Slavonic'],
  'Byzantium'     : ['Greek'],
  'Bisanzio'      : ['Greek'],
  'Rus'           : ['Slavonic'],
  'Russia'        : ['Slavonic'],
  'Britain'       : ['English', 'English', 'English', 'Welsh', 'French'],
  'Inghilterra'   : ['English', 'English', 'English', 'Welsh', 'French'],
  'Iberia'        : ['Spanish', 'Spanish', 'Spanish', 'Catalan', 'Portuguese', 'Arabic'],
  'Spagna'        : ['Spanish', 'Spanish', 'Spanish', 'Catalan', 'Portuguese', 'Arabic'],
  'Ireland'       : ['Gaelic', 'Gaelic', 'Gaelic', 'English'],
  'Irlanda'       : ['Gaelic', 'Gaelic', 'Gaelic', 'English'],
  'Scotland'      : ['Gaelic', 'Gaelic', 'English'],
  'Scozia'        : ['Gaelic', 'Gaelic', 'English'],
  'Levant'        : ['Arabic', 'Arabic', 'Hebrew', 'French'],
  'Levante'       : ['Arabic', 'Arabic', 'Hebrew', 'French'],
}


surnames_by_profession = {
'Shortbowman' : {
   'Italian' : ["l'Arciere"],
   'English' : ["Bowman", 'Archer'],
   'Latin'   : ['Sagittarius'],
   'Portuguese' : ['o Arqueiro'],
   'Occitan' : ["L'Arquièr"],
   'Occitan' : ["L'Arquer"],
},
'Huntsman' : {
   'Italian' : ['il Cacciatore'], 
   'English' : ['Hunter', 'Forester', 'Faulkner'],
   'German'  : ['Jaeger'],
   'French'  : ['Fauconnier', 'Le Chausser', 'Forestier'],
   'Slavonic': ['Lovach'],
   'Latin'   : ['Venator'],
},
'Scribe' : {
   'Italian' : ['lo Scrivano'], 
   'English' : ['Scrivener', 'Clark'],
   'Spanish' : ['Escribano'],
   'German'  : ['Schreiber'],
   'French'  : ['Le Clercq', 'Le Clerc'],
   'Greek'   : ['Chartoularios'],
},
'Mason': {
   'Italian' : ['il Muratore'], 
   'English' : ['Mason', 'Brickman'],
   'Romanian': ['Zidaru'],
   'German'  : ['Ziegler'],
}, 
'Carpenter': {
   'French'  : ['Charpentier', 'Caron', 'Carpentier'],
   'Italian' : ['il Carpentiere', 'il Falegname', 'il Legnaiuolo'], 
   'English' : ['Carpenter','Sawyer','Wright'],
   'Slavonic': ['Cieslar','Kolar','Plotnik','Stolyar'],
   'Romanian': ['Lemnaru', 'Dulgheru'],
   'German'  : ['Saeger','Zimmermann'],
   'Welsh'   : ['Saer'],
   'Latin'   : ['Carpentarius'],
   'Spanish' : ['Carpintero'],
   'Catalan' : ['Carpentier'],
}, 
'Cobbler': {
   'Italian' : ['il Ciabattino', 'il Conciatore'], 
   'Spanish' : ['Zapatero'],
   'Catalan' : ['Sapater'],
   'Occitan' : ['Sabatier'],
   'English' : ['Cobbler','Shoemaker'],
   'Romanian': ['Paslaru', 'Ciobotaru'],
   'French'  : ['le Péletier'],
   'German'  : ['Schuhmacher', 'Schuster'],
   'Slavonic': ['Shevts'],
   'Latin'   : ['Sutor'],
}, 
'Cooper': {
   'Italian' : ['il Bottaio', 'il Bottaro'], 
   'English' : ['Cooper'],
   'Slavonic': ['Bondar','Kachar'],
   'German'  : ['Kubel', 'Boettcher', 'Fassbinder'],
   'Romanian': ['Botar', 'Butaru', 'Dogaru'],
}, 
'Blacksmith': {
   'French'  : ['Fabron', 'le Frevre', 'Favre'],
   'Italian' : ['il Fabbro'],
   'English' : ['Smith'],
   'Spanish' : ['Ferreiro','Herrero'],
   'Portuguese' : ['Ferreiro'],
   'Catalan' : ['Ferrer'],
   'German'  : ['Schmidt', 'Hammerschmidt','Pinkert','Schlegel'],   
   'Romanian': ['Fieraru'],
   'Slavonic': ['Kutnets','Koval','Kovach'],
   'Catalan' : ['Ferrièr'],
   'Welsh'   : ['Of', 'Gof'],
   'Latin'   : ['Faber'],
   'Occitan' : ['Fabre', 'Faure', 'Fauré'],
}, 
'Brewer': {
   'Italian' : ['il Birraio'],
   'German'  : ['Breuer'],   
   'English' : ['Brewer', 'Brewster'],
}, 
'Vintner': {
   'Italian' : ['il Vinattiere','il Vinaio','il Vignaiolo'], 
   'English' : ['Vintner', 'Gartner'],
   'German'  : ['Keller','Weingartner'],
   'French'  : ["le Vigneron"],
}, 
'Cheesemaker': {
   'Italian' : ['il Formaggiaio'],
   'English' : ['Cheeseman'],
   'French'  : ['le Fourmagier'],
}, 
'Tinker': {
   'English' : ['Iremonger','Coppersmith'],
   'German'  : ['Kesselmann', 'Kessler','Kleinschmidt', 'Klemperer', 'Schlosser'],
   'French'  : ["le Cloutier"],
   'Italian' : ["l'Arrotino", 'il Magnano', 'lo Stagnino'],
   'Catalan' : ['Manyà'],
}, 
'Weaver': {
   'French'  : ['le Coutourier', 'le Parmentier'],
   'English' : ['Weaver', 'Taylor', 'Glover', 'Fuller', 'Hosier'],
   'Slavonic': ['Kadlec','Kozhel','Krajchik','Kravets','Portnoy','Tkach'],
   'Italian' : ['il Sarto', 'il Tessitore', 'il Tintore'],
   'German'  : ['Schneider', 'Schnider','Weber','Wollner', 'Schroeder'],
   'Welsh'   : ['Skynith', 'Skinnith'],
   'Catalan' : ['Teissier'],
   'Occitan' : ['Teissièr'],
   'Greek'   : ['Blattion'],
}, 
'Goldsmith': {
   'Italian' : ["Orefice" , "l'Orafo"],
   'English' : ['Goldsmith'],
   'German'  : ['Goldschmidt', 'Goldschmitt'],
   'Slavonic': ['Zolotar'],
   'Latin'   : ['Aurifaber'],
   'French'  : ["le Prud'homme"],
   'Greek'   : ['Aurifices'],
}, 
'Glassblower': {
   'English' : ['Glazer', 'Glaser', 'Glazier'],
   'German'  : ['Glaser' ],
   'French'  : ['le Boutilier'],
}, 
'Butcher': {
   'French'  : ['le Boucher'],
   'English' : ['Butcher'],
   'German'  : ['Fleischner'],
   'Italian' : ['il Macellaio'],
   'Slavonic': ['Masar','Reznik'],
   'Spanish' : ['Verdugo', 'Carnicero'],
   'Romanian': ['Macelaru'],
}, 
'Armorer': {
   'Italian' : ["l'Armaiolo"],
   'French'  : ["le Prud'homme"],
   'English' : ['Homer'],
}, 
'Swordsmith': {
   'Italian' : ['lo Spadaio', 'Spadaro'],
   'English' : ['Smith','Cutler','Naysmith'],
   'German'  : ['Messerschmidt', 'Messer'],
   'French'  : ["le Prud'homme"],
}, 
'Bowyer': {
   'English' : ['Bowman', 'Fletcher', 'Bowyer'],
   'German'  : ['Fiederer'],
},
'Reeve': {
   'English' : ['Reeves', 'Constable','Reeve','Granger'],
   'German'  : ['Meyer','Schultz'],
   'Italian' : ['il Balivo', 'il Fattore', "l'Intendente"],   
}, 
'Sailor': {
   'Italian' : ['il Marinaio', 'il Nostromo', 'il Barcaiolo'],
   'German'  : ['Steuermann'],
   'French'  : ['le Marinier'],
}, 
'Steward': {
   'English' : ['Steward', 'Despencer','Proctor','Greyve'],
   'German'  : ['Hoffmann'],
   'English' : ['Boatman'],
   'Occitan' : ['lo Cellarier', 'lo Despensier'],
   'Greek'   : ['Apothekarios'],
}, 
'Teamster': {
   'French'  : ['le Marchand', 'le Mercier', 'le Charretier', 'le Portéeur'],
   'Italian' : ['il Mulattiere', 'il Carrettiere'],
   'German'  : ['Handelsman','Kaufmann','Kutscher','Wagner', 'Fuhrmann'],
   'English' : ['Carter', 'Porter', 'Wagoner', 'Cartwright'],
   'Catalan' : ['Boyer', 'Boyé', 'Bouyer'],
}, 
'Chamberlain': {
   'French'  : ['Page', 'Le Page'],
   'Italian' : ['il Ciambellano', 'il Paggio'],
   'English' : ['Chamberlain', 'Butler'],
   'Greek'   : ['Koubikoularios'],
},
'Laborer' : {
   'English' : ['Fisher', 'Coulthard', 'Hunter', 'Cowherd', 'Harrier', 'Collier', 'Milner', 'Miller', 'Gardener', 'Shepherd'],
   'German'  : ['Schaefer', 'Bauer', 'Fischer', 'Hoffmann', 'Baumann', 'Kohler', 'Mueller', 'Egger', 'Geissler', 'Hauer', 'Hofer' ], 
   'French'  : ['le Pasteur', 'le Vachon', 'le Bouvier', 'le Pescheur', 'le Meunier', 'le Poissonier' ],
   'Romanian': ['Bouariu', 'Pescaru'],
   'Occitan' : ['Boyer', 'Boyé', 'Bouyer', 'Palomer', 'lo Carbonier', 'lo Castanier', 'Espalhat', 'Pagès', 'Pan'],
   'Italian' : ['il Cacciatore', 'il Pescatore', 'il Mugnaio', 'il Pastore', 'il Pecoraio', 'il Capraio', 'il Contadino'],
},
'Servant' : {
   'English' : [ 'Baker', 'Cook', 'Barber' ],
   'German'  : [ 'Becker', 'Koch' ], 
   'French'  : [ 'le Boulanger', 'le Fournier', 'le Lavendièr' ],
   'Italian' : [ 'il Fornaro', 'il Cuoco', 'il Servo', 'il Servitore', 'il Cameriere', 'il Lavandaio', 'il Pasticcere', 'il Valletto', 'il Panettiere' ],
   'Occitan' : [ 'Charrier', 'Pagès', 'lo Fogasier', 'lo Fornier', 'lo Lavandier', 'lo Fenassier', 'lo Pastesier', 'lo Servent', 'lo Vaylet', 'lo Bugadier', 'lo Camarier'],
   'Greek'   : ['Balnitor'],
},
}

surnames_by_profession_female = {
'Shortbowman' : {
   'Italian' : ["l'Arciera"],
   'Latin'   : ['Sagittaria'],
   'Portuguese' : ['a Arqueira'],
   'Occitan' : ["L'Arquièra"],
},
'Huntsman' : {
   'Italian' : ['la Cacciatrice'], 
   'French'  : ['la Fauconniere', 'La Chausseuse'],
   'Latin'   : ['Venatrix'],
},
'Scribe' : {
   'Italian' : ['la Scrivana'], 
   'Spanish' : ['Escribana'],
},
'Mason': {
   'Italian' : ['la Muratrice', 'la Muratora'], 
}, 
'Carpenter': {
   'Italian' : ['la Carpentiera', 'la Legnaiuola', 'la Falegname'], 
   'Latin'   : ['Carpentaria'],
   'Spanish' : ['Carpintera'],
}, 
'Cobbler': {
   'Italian' : ['la Ciabattina', 'la Conciatrice'], 
   'Occitan' : ['la Sabatiera'],
   'Latin'   : ['Sutrix'],
}, 
'Cooper': {
   'Italian' : ['la Bottaia', 'la Bottara'], 

}, 
'Blacksmith': {
   'Occitan' : ['Ferriera'],
}, 
'Brewer': {
   'Italian' : ['la Birraia'],
}, 
'Vintner': {
   'Italian' : ['la Vinattiera','la Vinaia','la Vignaiola'], 
}, 
'Cheesemaker': {
   'Italian' : ['la Formaggiaia'],
}, 
'Tinker': {
}, 
'Weaver': {
   'Italian' : ['la Sarta', 'la Tessitrice'],
   'Occitan' : ['la Teissièra'],
}, 
'Goldsmith': {
   'Italian' : ["l'Orefice" , "l'Orafa"],
}, 
'Glassblower': {
}, 
'Butcher': {
   'Italian' : ['la Macellaia'],
   'Spanish' : ['la Carnicera'],
}, 
'Armorer': {
   'Italian' : ["l'Armaiola"],
}, 
'Swordsmith': {
   'Italian' : ['la Spadaia', 'Spadara'],
}, 
'Bowyer': {
},
'Reeve': {
   'Italian' : ['la Baliva', "l'Intendente"],   
}, 
'Sailor': {
   'Italian' : ['la Marinara', 'la Nocchiera', 'la Barcaiola'],
}, 
'Steward': {
   'Italian' : ['la Dispensiera'],
   'Occitan' : ['la Cellariera', 'la Despensiera'],
   'Greek'   : ['Apothekarie'],
}, 
'Teamster': {
   'Italian' : ['la Mulattiera', 'la Carrettiera'],
}, 
'Chamberlain': {
   'Italian' : ['la Ciambellana'],
   'Greek'   : ['Koubikoularie'],
},
'Laborer' : {
   'Occitan' : ['Boyer', 'Boyé', 'Bouyer', 'Palomer', 'la Carboniera', 'la Castaniera', 'Espalhat', 'Pagès', 'Pan'],
   'Italian' : ['la Cacciatrice', 'la Cacciatora', 'la Pescatrice', 'la Pescatora', 'la Mugnaia', 'la Pastora', 'la Pecoraia', 'la Capraia', 'la Contadina'],
},
'Servant' : {
   'Italian' : [ 'la Fornara', 'la Cuoca', 'la Serva', 'la Panettiera', 'la Pasticcera', 'la Cameriera', 'la Lavandaia' ],
   'Occitan' : [ 'la Fogasiera', 'la Forniera', 'la Lavandiera', 'la Fenassiera', 'la Pastesiera', 'la Serventa', 'la Vayleta', 'la Bugadiera', 'la Camariera'],
   'French'  : [ 'la Lavendière', 'la Chambrière'  ],
},
}

surnames_by_profession['Longbowman'] = surnames_by_profession['Shortbowman']
surnames_by_profession_female['Longbowman'] = surnames_by_profession_female['Shortbowman']

estates_by_language = {
'Italian' : ["da Riva", "d'Acquaviva", "da Agrate", "d'Aiello", "d'Albano", "d'Albaredo", "di Alessandria", "d'Anguillara", "di Anzano", "d'Appiano", "d'Ariano", "di Arquata", "d'Azzano", 'da Badia', "da Bagnoli", "di Barbarano", "da Barberino", "da Bassano", "di Belforte", "di Belmonte", "da Berzo", "da Borghetto", "da Brignano", "da Cagnano", "di Calvi", "di Camerano", "di Campagnola", "da Campiglia", "da Campobello", "da Campofelice", "da Campolongo", "di Campoli", "di Candia", "da Cantalupo", "da Carbonara", "da Carpineto", "di Carpignano", "di Casale", "da Casanova", "di Cassano", "da Castagneto", "di Castelfranco", "da Castellana", "di Castelletto", "da Castelnovo", "di Castelnuovo", "di Castelvecchio", "da Castiglione", "da Celle", "dal Cerreto", "da Cerro", "da Chiaravalle", "di Civitella", "del Colle", "da Diano", "da Fagnano", "di Falconara", "di Fara", "da Fiumefreddo", "da Foiano", "di Fontaneto", "da Fossalto", "da Fornovo", "di Francavilla", "da Gagliano", "da Gallicano", "da Gravina", "di Grumo", "da Lama", "da Laureana", "di Livo", "da Longone", "da Macchia", "da Magliano", "da Mandello", "da Marano", "da Massa", "da Mazzano", "di Melito", "da Mezzana", "da Minervino", "di Mirabello", "di Monforte", "da Montalbano", "da Montaldo", "da Montalto", "di Montecchio", "di Montechiaro", "di Montefalcone", "di Monteforte", "da Montegrosso", "di Monteleone", "di Montenero", "di Monterosso", "da Montesano", "di Monteverde", "da Monticello", "da Montorio", "di Motta", "da Nocera", "di Nova", "d'Olgiate", "da Oliveto", "d'Olevano", "d'Orsara", "da Paderno", "di Palazzolo", "di Penna", "da Piedimonte", "da Pieve", "del Poggio", "da Ponte", "di Prata", "di Quarto", "da Quinto", "da Rignano", "di Rionero", "di Ripalta", "di Rivalta", "da Robecco", "della Rocca", "di Roccaforte", "da Rocchetta", "da Romano", "da Ronco", "da Roseto", "di Rosignano", "di Sala", "da Sale", "di Salza", "da San Benedetto", "di San Biagio", "di San Cipriano", "di San Damiano", "di San Daniele", "di San Donato", "di San Felice", "di San Giacomo", "di San Giorgio", "di San Giovanni", "di San Giuliano", 'di San Gregorio', "di San Lorenzo", "di San Marco", "di San Martino", "di San Mauro", "di San Michele", "di San Paolo", "di San Pietro", "di San Salvatore", "di San Vito", "di Sant'Agata", "di Sant'Ambrogio", "di Sant'Angelo", "di Sant'Andrea", "di Sant'Eufemia", "di Santa Croce", "di Santa Maria", "di Santa Sofia", "di Santo Stefano", "di Savignano", "da Selva", "da Serravalle", "da Sesto", "da Settimo", "di Somma", "di Spigno", "di Terranova", "da Torella", "di Torrevecchia", "di Torricella", "di Tramonti", "di Vaglio", "da Vaiano", "da Valeggio", "da Varano", "di Vezzano", "di Vignola", "da Villafranca", "da Villanova", "di Ziano" ],
'Occitan' : ["de l'Ilha", "de Cabaretz", "de Termes", "de Montréal", "de Boclo", "de Crion", "de Lebret", "de Luset", "de Luces", "de Roca Negada", "de Roci", "de Bles", "de Blanchafort", "de Montagut", "de Vilamur", "d'Aspel", "de Caldairon", "de Sentlir", "de Lomahna", "de Caro", "de Corneus", "de Montesquiou", "de Montpezat", "de Casnac", "de Cumenge", "d'Esgal", "de Marestahns", "de Montaut", "de Rocafort", "de Sent Marti", "de Saisches", "de Palhares", "d'Avinho", "de Cardelhac", "de Corsson", "de Gordo", "de Monester", "de Pestilhac", "de Tholoza", "de Campanha", "d'Uzest", "d'Albaroca", "de La Barta", "de Linars", "de Caus", "de Vilapros", "d'Angelier", "de Berzi", "d'Astaragues", "de Creiselh", "de Merlon", "de Lacis", "de Laens", "de La Mota", "de Montelh", "del Brolh", "de Pontos", "de l'Aia", "de Punhtis", "de Pui Laurens", "de Dia", "de Bolho", "de Cambrais", "de Pradeus", "de La Treua", "de Malbusson", "de Monfavens", "de Lavaur", "de Peitieus", "de Galbert", "de Berlit", "de Niort", "de Toges", "de Saiches", "de Minerba", "de Rocas", "d'Encontre", "de La Barra", "de Montlaur", "de Mauros", "de Pepios", "de Gordos", "de Cavalho", "de Mauretanha", "dels Armes", "d'Olitz", "de Luzia", "de Sent Beat", "de Saissi", "de Rabastens", "de Durban", "de Lambesc", "de la Isla", "d'Escorralha", "de Seguret", "de Sent Prais", "de Castelnou", "de Breumont", "de Mondragos", "de Sent Just", "de la Calm", "de las Bordas", "de Peirigorc", "de Montalba", "de Rocafolhs", "de Rabastencs", "de Salvanhac", "de Vals", "de Castelbo", "del Gua", "de Niela", "de Caudaros", "de Trias", "de Tornados", "de Lhineiras", "de l'Issart", "del Pugal", "de Carboneiras", "de Malleo", "de Balencs", "de Pog Laurens", "dels Juratz", "de Nouvila", "d'Orion", "de Blezon", "de Bar" ],
'French'  : ['de Monfort', 'de Guines', 'de Brienne', 'de Bellegarde', 'de Beaumont', "d'Ancerville", 'de Pierrepont', ' de Chantilly', 'de Chatillon', 'de Saint-Jacques', 'de Clermont', 'de Craon', 'de Couchy', 'de Corbeil', 'de La Valette', 'de Chalon', 'de Lancre','de Picquigny', 'de Houdetot', 'de Doué', 'de La Bussière', 'du Merle', 'de Ceriz', "d'Auffay", 'de Ribemont', 'de Roquelaure', 'de Champignelles', 'de Béthune', 'de Dol', 'de Coucy', 'de Ligny', 'de Carency', 'de Clisson', 'de Saint-Just', 'de Malouet', 'de Treil', 'de Jessé', 'de Coubertin', 'de Caumont', 'de Brandois', 'de Damas', 'du Creux', 'de Gramont', 'de Gobineau', "d'Estaing", "d'Evreux", "d'Eu", "d'Autun", 'de Cagny', 'de Rochambeau', 'de Tessé', "d'Autigny", "d'Aubigné", "de Brézé", 'de Créquy', 'de Noyelles', 'de Troyes', "d'Aunay", "de la Corne", "de la Touche", "de Laumoy", 'de Vogué', "d'Arlincourt", "de Noailles", "de Montgomery", "de Léry", "de Servières", "de Mauduit", "de Chatellerault", 'de Clare', 'de Valence', 'du Plessis', 'de Beauchamp', 'de Montagu', 'de Monthermer', 'de Blondeville', 'de Ferrers', 'de Bohun', 'de Quincy', "d'Auberville", 'de Criol', 'de Crevecoeur', 'de Moels', 'de Rivaux', 'de Gernon', 'de Courcy' ],
'English' : ['de Fulbourn', 'de Ferings', 'de Boderisham', 'de Kirkeby', 'de Grey', 'de Pencester', 'de Leybourne', 'de Sandwich', 'de Fauconberg', 'de Mandeville', 'de Braose', 'de Segrave', 'de Redvers', 'de Chesney', 'de Clifford', 'de Berkeley', 'de Gorham'],
'Portuguese' : ['de Brito', 'de Briteiros', 'de Melo', 'de Lobeira', 'de Haro', 'de Serpa', 'de Riba', 'de Leiria', 'de Albuquerque', 'de Meneses', 'de Alenquer', 'de Orduna', 'de Soverosa', 'de Freitas', 'de Sartarém', 'de Leomil', 'de Valadares', 'de Santa Cruz', 'de Viana', 'de Redondo', 'de Abrantes', 'de Alvor', 'de Bracial', 'de Faro', 'de Feira', 'de Torres', 'de Neiva', 'de Ourém', 'de Vila Nova', 'de Vila Real', 'de Ameal', 'de Almada', 'de Portalegre', 'de Vasconcelos', 'de Moura', 'de Viseu', 'de Travassos'],
#'Catalan' : [],
}

german_locative_prefixes = ['Bachen', 'Bircken', 'Elwan', 'Selgen', 'Gruenin', 'Rein', 'Krewels', 'Oden', 'Oster', 'Poppen', 'Plancken', 'Pfaffen', 'Obern', 'Massen', 'Leim', 'Stein', 'Thenin', 'Wollfers', 'Wyppin', 'Yge', 'Durren', 'Hass', 'Still', 'Moner', 'Hinter', 'Roren', 'Hor', 'Ravens', 'Pforz', 'Branden', 'Rends', 'Salz', 'Roten', 'Gruenen', 'Blauen', 'Sege', 'Nuren', 'Olden', 'Uren', 'Eisen', 'Rue']
german_locative_suffixes = ['dorf', 'heim', 'stat', 'gen', 'tal', 'zell', 'hoff', 'fels', 'feld', 'bach', 'brun', 'lach', 'burg', 'berg']

estates_by_language['German'] = sum([ [ p+s for p in german_locative_prefixes ] for s in german_locative_suffixes ],[])
estates_by_language['English'] += estates_by_language['French']


autorita = ['Agricola', 'Agrippa', 'Albicus', 'Aliacensis', 'Alemannus', 'Anglicus', 'Antiquus', 'Aquila', 'Aquitanus', 'Archicancellarius', 'Archidiaconus', 'Archipoeta', 'Archypresbiter', 'Ardens', 'Ariminensis', 'Augustodunensis', 'Aventinus', 'Aurelianensis', 'Aureolus', 'Badonicus', 'Balbulus', 'Balbus', 'Barensis', 'Bavarus', 'Bellovacensis', 'Bibliothecarius', 'Biclarensis', 'Bobiensis', 'Bononiensis', 'Bracarensis', 'Brito', 'Burgulianus', 'Cambrensis', 'Campanus', 'Cancellarius', 'Cantabrigiensis', 'Cantipratensis', 'Capellanus', 'Casinensis', 'Castrensis', 'Catinensis', 'Cenomanensis', 'Claramontanus', 'Claravallensis', 'Clericus', 'Compostellanus', 'Contractus', 'Corvinus', 'Crassus', 'Cremonensis', 'Dacus', 'Damianus', 'Diaconus', 'Dolensis', 'Dumiensis', 'Faber', 'Ferrariensis', 'Floriacensis', 'Fortunatus', 'Frisingensis', 'Fuldensis', 'Gallus', 'Gemblacensis', 'Glaber', 'Glocestriensis', 'Graecus', 'Grammaticus', 'Grassus', 'Gundissalinus', 'Halensis', 'Heisterbacensis', 'Hibernicus', 'Hierosolimitanus', 'Hispanus', 'Historicus', 'Iudaeus', 'Iudex', 'Januensis', 'Junior', 'Ketenensis', 'Laetus', 'Latinus', 'Lombardus', 'Lugdunensis', 'Luxoviensis', 'Lyranus', 'Magnus', 'Maius', 'Malmesburiensis', 'Massiliensis', 'Maurus', 'Mettensis', 'Minor', 'Modicus', 'Mogontinus', 'Monachus', 'Monemutensis', 'Montanus', 'Nauclerus', 'Nigellus', 'Niger', 'Notarius', 'Oppaviensis', 'Pannonius', 'Panormitanus', 'Parisiensis', 'Patavinus', 'Pauper', 'Peregrinus', 'Physicus', 'Pisanus', 'Platearius', 'Polonus', 'Puteanus', 'Ravennatis', 'Redoniensis', 'Reicherspergensis', 'Rievallensis', 'Romanus', 'Rothomagensis', 'Sagax', 'Saresberiensis', 'Saxo', 'Scholasticus', 'Scotus', 'Secundus', 'Senior', 'Septimellensis', 'Servatus', 'Silvestris', 'Strabo', 'Symphosius', 'Teutonicus', 'Tiburtinus', 'Tilberiensis', 'Toletanus', 'Tortarius', 'Tranensis', 'Triumphus', 'Turonensis', 'Tyrensis', 'Ursinus', 'Veneticus', 'Veronensis', 'Vitalis', 'Viterbensis', 'Vorminientis', 'Vulcanius', 'Vulgarius', 'a Gandavo', 'ab Insulis', 'de Messina', 'de Monte', 'de Sacrobosco', 'de Sancto Victore', 'de Vineas']

languages = sorted(list(names['male'].keys()))

def get_auctoritas_surname(gender='male'):
  s = choice(autorita)
  if gender=='female' :
    if s[-2:]=='us' : return s[:-2]+'a'
    if s[-2:]=='er' : 
      if s[-3] in 'tp' : return s+'a'
      else : return s[:-2]+'ra'
  return s

def get_surname_base(gender, language):
  f = get_name('male', language, surname=False)
  if language in [ 'Spanish', 'Portuguese' ]:
    s = 's'
    if language in ['Spanish'] and choice([1,1,0]): s = 'z'
    while 1:
      if f[-2:] == 'ia'  : return f[:-2]+'e'+s
      if f[-2:] == 'io'  : return f[:-2]+'e'+s
      if f[-3:] == 'dro' : return f[:-3]+'re'+s
      if f[-3:] == 'ego' : return f[:-2]+s
      if f[-2:] == 'go'  : return f[:-1]+'ue'+s
      if f[-2:] == 'co'  : return f[:-2]+'que'+s
      if f[-1] in [ 'e', 'a' ] : return f+s
      if f[-1] == 'o' : return f[:-1]+'e'+s
      if f[-1] in [ 'n', 'l' ] : return f+'e'+s
      f = get_name('male', language)
  if language in [ 'Catalan', 'Occitan' ] and gender=='male':
    return f
  if language in [ 'Gaelic' ] and gender=='male':
    return choice(['Mac ', "O'"])+f
  if language in [ 'Gaelic' ] and gender=='female':
    return choice(['Nic ', "O'"])+f
  if language in [ 'Welsh' ] and gender=='male':
    return choice(['ap ', "ab ", 'filius '])+f
  if language in [ 'Welsh' ] and gender=='female':
    return choice(['verch ', "filia ", 'wreich ', 'uxor '])+f
  if language in [ 'Norse' ] and gender=='male':
    return f+'sson'
  if language in [ 'Norse' ] and gender=='female':
    return f+'sdottir'
  if language in [ 'Slavonic' ] and gender=='male':
    if f[-1] in 'sl' : return f+'evic'
    if f[-1] == 'v' : return f+'ic'
    if f[-1] in 'prmfnk' : return f+'ovic'
    return f+'vic'
  if language in [ 'Slavonic' ] and gender=='female':
    if f[-1] in 'sl' : return f+'ova'
    if f[-1] == 'v' : return f+'ica'
    if f[-1] in 'prmfnkd' : return f+'ova'
    return f+'vica'
  if language in [ 'French' ]:
    return choice(['de ',''])+f
  if language == 'Italian' :
    if choice([0,1,1]): 
      if f[0] in 'AEIOU' : return "d'"+f
      else: return 'di '+f
    p = 'dei '
    if f[0] in 'AEIOUJZ' or f[0] == 'S' and f[1] not in 'aeiou' : p='degli '
    if f[-2:] == 'co' or f[-2:] == 'go' : return p+f[:-1]+'hi'
    if f[-2:] == 'io' : return p+f[:-1]
    return p+f[:-1]+'i'
  if language == 'Latin' :   
    f = get_name(gender, language, surname=False)
    return f
  if language == 'English' :
    if f[-1] in 'pdrmt' : return f+'s'
    return 'fitz '+f
  if language == 'Arabic' and gender=='male' : 
    suffix = choice(['ibn ', '', 'bin '])
    if len(suffix): return suffix+f
  if language == 'Arabic' and gender=='female' : 
    suffix = choice(['', 'bint '])
    if len(suffix): return suffix+f
  return ''

professions = sorted(['Nobleman', 'Knight', 'Gentleman', 'Noblewoman', 'Troubador', 'Priest']+ list(surnames_by_profession.keys()))

print(languages)
print(professions)

def get_surname(gender, language, profession=None):
  if profession :
    if profession == 'random' : profession = choice(professions)
    if choice([1,1,0]) :
      try : 
        if language == 'Latin' : return get_auctoritas_surname(gender)
        if gender == 'female' and language in surnames_by_profession_female[profession]:
          return choice(surnames_by_profession_female[profession][language])      
        return choice(surnames_by_profession[profession][language])
      except Exception : pass
  s = get_surname_base(gender, language)
  if profession in ['Nobleman', 'Knight', 'Gentleman', 'Noblewoman', 'Troubador', 'Priest'] :
    try : s += (' ' if language != 'German' else choice(['von ', 'von ', 'zu ']))+choice(estates_by_language[language])
    except Exception : pass 
  return s


ita_to_eng_lang = {
  'Arabo'      : 'Arabic',
  'Basco'      : 'Basque',
  'Catalano'   : 'Catalan',
  'Inglese'    : 'English',
  'Francese'   : 'French',
  'Gaelico'    : 'Gaelic',
  'Tedesco'    : 'German',
  'Greco'      : 'Greek',
  'Ebraico'    : 'Hebrew',
  'Ungherese'  : 'Hungarian',
  'Italiano'   : 'Italian',
  'Latino'     : 'Latin',
  'Scandinavo' : 'Norse',
  'Provenzale' : 'Occitan',
  'Portoghese' : 'Portuguese',
  'Romeno'     : 'Romanian', 
  'Slavo'      : 'Slavonic',
  'Castigliano': 'Spanish',
  'Cimrico'    : 'Welsh',
}

ita_to_eng_prof = {
  'Armaiolo'   : 'Armorer',
  'Fabbro'     : 'Blacksmith',
  'Arcaio'     : 'Bowyer',
  'Birraio'    : 'Brewer',
  'Macellaio'  : 'Butcher',
  'Carpentiere': 'Carpenter',
  'Ciambellano': 'Chamberlain',
  'Formaggiaio': 'Cheesemaker',
  'Ciabattino' : 'Cobbler',
  'Bottaio'    : 'Cooper',
  'Cortigiano' : 'Gentleman',
  'Vetraio'    : 'Glassblower',
  'Orafo'      : 'Goldsmith',
  'Cacciatore' : 'Huntsman',
  'Cavaliere'  : 'Knight',
  'Bracciante' : 'Laborer',
  'Muratore'   : 'Mason',
  'Nobile'     : 'Nobleman',
  'Nobildonna' : 'Noblewoman',
  'Prete'      : 'Priest',
  'Funzionario': 'Reeve',
  'Marinaio'   : 'Sailor',
  'Copista'    : 'Scribe',
  'Servo'      : 'Servant',
  'Arciere'    : 'Shortbowman',
  'Amministratore' : 'Steward',
  'Spadaio'    : 'Swordsmith',
  'Carovaniere': 'Teamster',
  'Stagnaio'   : 'Tinker',
  'Trovatore'  : 'Troubador',
  'Vinattiere' : 'Vintner',
  'Sarto'      : 'Weaver',
}


def get_name(gender='male', language='Occitan', surname=True, profession='random'):
  # Support for Italian input
  if gender not in ['male','female'] : 
    if gender[0]=='m' : gender='male'
    else : gender = 'female'
  if language not in languages and language in ita_to_eng_lang :
    language=ita_to_eng_lang[language]
  if profession not in professions and profession in ita_to_eng_prof :
    profession=ita_to_eng_prof[profession]
  s = get_surname(gender, language, profession) if surname else ''
  if len(s) : s = ' '+s
  return choice(names[gender][language]) + s


  
if __name__ == '__main__':
  import argparse
  # Parse the command line arguments
  parser = argparse.ArgumentParser(
    prog='Medieval Name Generator',
    description='''Generate random names.'''
    )
  parser.add_argument('-g','--gender', default='male', choices=['male','female'], help='gender of name, defaults to male')
  parser.add_argument('-l','--language', default='Latin', choices=languages, help='Language of name, defaults to Latin')
  parser.add_argument('--surname', action=argparse.BooleanOptionalAction, default=True, help='include a surname')
  parser.add_argument('-p','--profession', default='random', choices=['random']+professions, help='Profession of the character (defaults to random)')
  args=parser.parse_args()
  #print(args)
  print(get_name(args.gender,args.language,args.surname,args.profession))
    
  
