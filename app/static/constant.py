"""Constants of the program."""


GOOGLE_API_KEY = "AIzaSyAe3gxU6P4vkZPHFiUUctnwdwWbxJ8u-Bo"


STOPWORD = [
    "a",
    "abord",
    "absolument",
    "afin",
    "ah",
    "ai",
    "aie",
    "ailleurs",
    "ainsi",
    "ait",
    "allaient",
    "allo",
    "allons",
    "allô",
    "alors",
    "anterieur",
    "anterieure",
    "anterieures",
    "apres",
    "après",
    "as",
    "assez",
    "attendu",
    "au",
    "aucun",
    "aucune",
    "aujourd",
    "aujourd'hui",
    "aupres",
    "auquel",
    "aura",
    "auraient",
    "aurait",
    "auront",
    "aussi",
    "autre",
    "autrefois",
    "autrement",
    "autres",
    "autrui",
    "aux",
    "auxquelles",
    "auxquels",
    "avaient",
    "avais",
    "avait",
    "avant",
    "avec",
    "avoir",
    "avons",
    "ayant",
    "b",
    "bah",
    "bas",
    "basee",
    "bat",
    "beau",
    "beaucoup",
    "bien",
    "bigre",
    "boum",
    "bravo",
    "brrr",
    "c",
    "car",
    "ce",
    "ceci",
    "cela",
    "celle",
    "celle-ci",
    "celle-là",
    "celles",
    "celles-ci",
    "celles-là",
    "celui",
    "celui-ci",
    "celui-là",
    "cent",
    "cependant",
    "certain",
    "certaine",
    "certaines",
    "certains",
    "certes",
    "ces",
    "cet",
    "cette",
    "ceux",
    "ceux-ci",
    "ceux-là",
    "chacun",
    "chacune",
    "chaque",
    "cher",
    "chers",
    "chez",
    "chiche",
    "chut",
    "chère",
    "chères",
    "ci",
    "cinq",
    "cinquantaine",
    "cinquante",
    "cinquantième",
    "cinquième",
    "clac",
    "clic",
    "combien",
    "comme",
    "comment",
    "comparable",
    "comparables",
    "compris",
    "concernant",
    "contre",
    "couic",
    "crac",
    "d",
    "da",
    "dans",
    "de",
    "debout",
    "dedans",
    "dehors",
    "deja",
    "delà",
    "depuis",
    "dernier",
    "derniere",
    "derriere",
    "derrière",
    "des",
    "desormais",
    "desquelles",
    "desquels",
    "dessous",
    "dessus",
    "deux",
    "deuxième",
    "deuxièmement",
    "devant",
    "devers",
    "devra",
    "different",
    "differentes",
    "differents",
    "différent",
    "différente",
    "différentes",
    "différents",
    "dire",
    "directe",
    "directement",
    "dit",
    "dite",
    "dits",
    "divers",
    "diverse",
    "diverses",
    "dix",
    "dix-huit",
    "dix-neuf",
    "dix-sept",
    "dixième",
    "doit",
    "doivent",
    "donc",
    "dont",
    "douze",
    "douzième",
    "dring",
    "du",
    "duquel",
    "durant",
    "dès",
    "désormais",
    "e",
    "effet",
    "egale",
    "egalement",
    "egales",
    "eh",
    "elle",
    "elle-même",
    "elles",
    "elles-mêmes",
    "en",
    "encore",
    "enfin",
    "entre",
    "envers",
    "environ",
    "es",
    "est",
    "et",
    "etant",
    "etc",
    "etre",
    "eu",
    "euh",
    "eux",
    "eux-mêmes",
    "exactement",
    "excepté",
    "extenso",
    "exterieur",
    "f",
    "fais",
    "faisaient",
    "faisant",
    "fait",
    "façon",
    "feront",
    "fi",
    "flac",
    "floc",
    "font",
    "g",
    "gens",
    "h",
    "ha",
    "hein",
    "hem",
    "hep",
    "hi",
    "ho",
    "holà",
    "hop",
    "hormis",
    "hors",
    "hou",
    "houp",
    "hue",
    "hui",
    "huit",
    "huitième",
    "hum",
    "hurrah",
    "hé",
    "hélas",
    "i",
    "il",
    "ils",
    "importe",
    "j",
    "je",
    "jusqu",
    "jusque",
    "juste",
    "k",
    "l",
    "la",
    "laisser",
    "laquelle",
    "las",
    "le",
    "lequel",
    "les",
    "lesquelles",
    "lesquels",
    "leur",
    "leurs",
    "longtemps",
    "lors",
    "lorsque",
    "lui",
    "lui-meme",
    "lui-même",
    "là",
    "lès",
    "m",
    "ma",
    "maint",
    "maintenant",
    "mais",
    "malgre",
    "malgré",
    "maximale",
    "me",
    "meme",
    "memes",
    "merci",
    "mes",
    "mien",
    "mienne",
    "miennes",
    "miens",
    "mille",
    "mince",
    "minimale",
    "moi",
    "moi-meme",
    "moi-même",
    "moindres",
    "moins",
    "mon",
    "moyennant",
    "multiple",
    "multiples",
    "même",
    "mêmes",
    "n",
    "na",
    "naturel",
    "naturelle",
    "naturelles",
    "ne",
    "neanmoins",
    "necessaire",
    "necessairement",
    "neuf",
    "neuvième",
    "ni",
    "nombreuses",
    "nombreux",
    "non",
    "nos",
    "notamment",
    "notre",
    "nous",
    "nous-mêmes",
    "nouveau",
    "nul",
    "néanmoins",
    "nôtre",
    "nôtres",
    "o",
    "oh",
    "ohé",
    "ollé",
    "olé",
    "on",
    "ont",
    "onze",
    "onzième",
    "ore",
    "ou",
    "ouf",
    "ouias",
    "oust",
    "ouste",
    "outre",
    "ouvert",
    "ouverte",
    "ouverts",
    "o|",
    "où",
    "p",
    "paf",
    "pan",
    "par",
    "parce",
    "parfois",
    "parle",
    "parlent",
    "parler",
    "parmi",
    "parseme",
    "partant",
    "particulier",
    "particulière",
    "particulièrement",
    "pas",
    "passé",
    "pendant",
    "pense",
    "permet",
    "personne",
    "peu",
    "peut",
    "peuvent",
    "peux",
    "pff",
    "pfft",
    "pfut",
    "pif",
    "pire",
    "plein",
    "plouf",
    "plus",
    "plusieurs",
    "plutôt",
    "possessif",
    "possessifs",
    "possible",
    "possibles",
    "pouah",
    "pour",
    "pourquoi",
    "pourrais",
    "pourrait",
    "pouvait",
    "prealable",
    "precisement",
    "premier",
    "première",
    "premièrement",
    "pres",
    "probable",
    "probante",
    "procedant",
    "proche",
    "près",
    "psitt",
    "pu",
    "puis",
    "puisque",
    "pur",
    "pure",
    "q",
    "qu",
    "quand",
    "quant",
    "quant-à-soi",
    "quanta",
    "quarante",
    "quatorze",
    "quatre",
    "quatre-vingt",
    "quatrième",
    "quatrièmement",
    "que",
    "quel",
    "quelconque",
    "quelle",
    "quelles",
    "quelqu'un",
    "quelque",
    "quelques",
    "quels",
    "qui",
    "quiconque",
    "quinze",
    "quoi",
    "quoique",
    "r",
    "rare",
    "rarement",
    "rares",
    "relative",
    "relativement",
    "remarquable",
    "rend",
    "rendre",
    "restant",
    "reste",
    "restent",
    "restrictif",
    "retour",
    "revoici",
    "revoilà",
    "rien",
    "s",
    "sa",
    "sacrebleu",
    "sait",
    "sans",
    "sapristi",
    "sauf",
    "se",
    "sein",
    "seize",
    "selon",
    "semblable",
    "semblaient",
    "semble",
    "semblent",
    "sent",
    "sept",
    "septième",
    "sera",
    "seraient",
    "serait",
    "seront",
    "ses",
    "seul",
    "seule",
    "seulement",
    "si",
    "sien",
    "sienne",
    "siennes",
    "siens",
    "sinon",
    "six",
    "sixième",
    "soi",
    "soi-même",
    "soit",
    "soixante",
    "son",
    "sont",
    "sous",
    "souvent",
    "specifique",
    "specifiques",
    "speculatif",
    "stop",
    "strictement",
    "subtiles",
    "suffisant",
    "suffisante",
    "suffit",
    "suis",
    "suit",
    "suivant",
    "suivante",
    "suivantes",
    "suivants",
    "suivre",
    "superpose",
    "sur",
    "surtout",
    "t",
    "ta",
    "tac",
    "tant",
    "tardive",
    "te",
    "tel",
    "telle",
    "tellement",
    "telles",
    "tels",
    "tenant",
    "tend",
    "tenir",
    "tente",
    "tes",
    "tic",
    "tien",
    "tienne",
    "tiennes",
    "tiens",
    "toc",
    "toi",
    "toi-même",
    "ton",
    "touchant",
    "toujours",
    "tous",
    "tout",
    "toute",
    "toutefois",
    "toutes",
    "treize",
    "trente",
    "tres",
    "trois",
    "troisième",
    "troisièmement",
    "trop",
    "très",
    "tsoin",
    "tsouin",
    "tu",
    "té",
    "u",
    "un",
    "une",
    "unes",
    "uniformement",
    "unique",
    "uniques",
    "uns",
    "v",
    "va",
    "vais",
    "vas",
    "vers",
    "via",
    "vif",
    "vifs",
    "vingt",
    "vivat",
    "vive",
    "vives",
    "vlan",
    "voici",
    "voilà",
    "vont",
    "vos",
    "votre",
    "vous",
    "vous-mêmes",
    "vu",
    "vé",
    "vôtre",
    "vôtres",
    "w",
    "x",
    "y",
    "z",
    "zut",
    "à",
    "â",
    "ça",
    "ès",
    "étaient",
    "étais",
    "était",
    "étant",
    "été",
    "être",
    "ô"
]

WESTWORLD_QUOTES = {
    'reply' : [
        "Tu t'es perdu l'ami? Tu cherches ton chemin?  ",
        "Tu as des histoires à me raconter l'ami?  ",
        "Tu vas devoir suivre le labyrinthe.  "
        "Avez-vous déjà remis en question la nature de votre réalité? ",
    ],
    'success': [
        "Bravo, mon ami. Il semble que vous soyez parvenu au centre du labyrinthe.  ",
        "Je suppose que les gens aiment lire sur les choses qu'ils veulent le plus et qu'ils expérimentent le moins.  ",
        "J'en ai vu des choses dans ma chienne de vie.  ",
        "Tous ces plaisirs violents auront une fin violente.  ",
        "La beauté est un leurre.  ",
        "Ce qui est réel est irremplaçable.  ",
        "Certaines personnes choisissent de voir la laideur de ce monde.  Le désarroi.  Je choisis d'en voir la beauté. De croire qu'il y a un ordre à nos vies, un but.  ",
        "J'aime à me souvenir de ce que mon père m'a appris.  Qu'à un moment ou à un autre, nous sommes tous de nouveaux arrivants dans ce monde.  ",
        "Tout est magique dans ce monde, excepté le magicien.  ",
        "Seuls les gens ennuyeux s'ennuient.  ",
        "Le problème, mon ami, c'est que ce que vous et moi faisons est si compliqué.  Nous pratiquons la sorcellerie.  Nous énonçons les mots justes.  Ensuite, nous créons la vie elle-même… à partir du chaos.  ",
        "J'ai toujours aimé les bonnes histoires.  Je pense que les histoires nous ennoblissent, qu'elles réoarent ce qui est brisé en nous et nous aident à devenir la personne que nous rêvions d'être.  Des mensonges qui nous en disent plus sur la réalité.  ",
        "C’est une chose difficile, de réaliser que toute votre vie n'est qu'une fiction hideuse.  ",
        "Folie du genre humain, il y a toujours un désir d'en savoir plus.  "
    ],
    'failure' : [
        "Le labyrinthe ne t'ai pas destiné.  ",
        "Si vous ne pouvez pas faire la différence, est-ce important que ce soit réel ou non? ",
        "Un homme dont on met 10 ans à corriger l'erreur, c'est un sacré mec.  "
        "De toute façon, j'ai toujours fait plus confiance au code qu'aux gens.  "
        "Le piano n'assassine pas le pianiste s'il n'aime pas la musique.  ",
        "Vous ne pouvez pas jouer à Dieu sans vous acoquiner avec le diable.  ",
        "L'évolution a forgé l'intégralité de la vie consciente sur cette planète en utilisant un seul outil…  L'erreur.  ",
        "Ça vous ait déjà arrivé d'avoir quelque chose sur le bout de la langue, mais plus vous essayez de vous en souvenir, plus cela vous échappe? ",
        "Le labyrinthe est le symbole même de la vie d’un homme.  Des choix qu'il fait, des rêves auxquels il s'accroche.  ",
        "Quelqu'un m'a dit un jour qu'il y avait un chemin pour tout le monde.  Et mon chemin me ramène à vous.  "
        "Les humains aiment croire qu’il y a quelque chose d’unique dans leur façon de percevoir le monde, mais la réalité c'est qu'ils vivent dans des boucles, aussi étroites et fermées que celles dans lesquelles évoluent des robots.  ",
        "Toute ma vie, je me suis vanté d’être un survivant. Mais la survie n'est qu'une autre boucle.  ",
    ]
}
