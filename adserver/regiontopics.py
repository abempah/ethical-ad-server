"""Our targeting data for topics & regions."""

topic_list = [
    "data-science",
    "backend-web",
    "frontend-web",
    "security-privacy",
    "devops",
    "python",
    "game-dev",
    "blockchain",
    "techwriting",
]

data_science = [
    "data-science",
    "datascience",
    "ml",
    "training-data",
    "model-training",
    "machine-learning",
    "machinelearning",
    "sentiment-analysis",
    "ai",
    "artificial-intelligence",
    "neural-net",
    "neural-nets",
    "data-analytics",
    "visualization",
    "data-visualization",
    "nlp",
    "object-detection",
    "computer-vision",
    "jupyter",
    "matplotlib",
    "deep-learning",
    "pytorch",
    "pydata",
    "opencv-python-library",
    "pandas",
    "numpy",
    "tensor",
    "tensorflow",
]

backend_web = [
    "backend",
    "backend-web",
    "flask",
    "django",
    "werkzeug",
    "wsgi",
    "celery",
    "jinja",
]

frontend_web = [
    "frontend",
    "frontend-web",
    "javascript",
    "react",
    "reactjs",
    "css",
    "angular",
    "angularjs",
    "jquery",
    "vuejs",
    "vue",
    "webpack",
    # Debatably frontend
    "node",
    "nodejs",
]

security_privacy = ["security", "privacy", "cryptography", "oauth"]

devops = [
    "devops",
    "cloud",
    "docker",
    "kubernetes",
    "container",
    "containers",
    "ansible",
    "serverless",
    "openshift",
    "aws",
    "linux",
    "ubuntu",
    "monitoring",
    "openid-connect",
    "oauth",
    "redis",
    "rabbitmq",
    "nosql",
    "postgres",
    "postgresql",
    "mysql",
    "database",
    "elasticsearch",
    "lucene",
    "solr",
    "terraform",
    "nginx",
]

python = ["python", "django", "flask"]

game_dev = ["gamedev", "minecraft", "godot", "game"]

blockchain = [
    "blockchain",
    "ethereum",
    "bitcoin",
    "cryptocurrency",
    "hyperledger",
    "solidity",
]

# This will be heavily dominated by markdownguide which usually underperforms
# Be a bit careful
techwriting = ["technical-writing", "sphinx", "sphinx-doc", "mkdocs"]

## Geography
region_list = [
    "us-ca",
    "eu-aus-nz",
    "wider-apac",
    "latin-america",
    "africa",
    "exclude",
    "global",
]
us_ca = ["US", "CA"]

eu_aus_nz = [
    "DE",
    "GB",
    "FR",
    "IT",
    "ES",
    "CH",
    "NL",
    "PT",
    "AT",
    "BE",
    "LU",
    "IE",
    "GR",
    "SE",
    "DK",
    "NO",
    "FI",
    # Vaguely Eastern Europe but still EU
    "PL",
    "LV",
    "LT",
    "EE",
    "BG",
    "HR",
    "RO",
    "SK",
    "SI",
    "HU",
    "CZ",
    # Bundled into Europe
    "IL",
    # Australia and New Zealand
    "AU",
    "NZ",
]

# This is the more expensive regions in APAC
wider_apac = [
    "SG",
    "HK",
    "JP",
    "KR",
    "TW",
    # Australia and New Zealand
    "AU",
    "NZ",
]

latin_america = [
    "AI",
    "AR",
    "AW",
    "BS",
    "BB",
    "BZ",
    "BM",
    "BO",
    "VG",
    "KY",
    "CL",
    "CO",
    "CR",
    "CU",
    "CW",
    "DM",
    "DO",
    "EC",
    "SV",
    "FK",
    "GL",
    "GP",
    "GT",
    "GY",
    "HT",
    "HN",
    "JM",
    "MX",
    "MS",
    "NI",
    "PA",
    "PY",
    "PE",
    "PR",
    "BL",
    "KN",
    "LC",
    "MF",
    "PM",
    "VC",
    "SR",
    "TT",
    "UY",
    "VE",
    # Brazil which is sometimes separated
    "BR",
]

africa = [
    "DZ",
    "AO",
    "BJ",
    "BW",
    "BF",
    "BI",
    "CM",
    "CV",
    "CF",
    "KM",
    "CD",
    "DJ",
    "EG",
    "GQ",
    "ER",
    "ET",
    "GA",
    "GM",
    "GH",
    "GN",
    "GW",
    "CI",
    "KE",
    "LS",
    "LR",
    "LY",
    "MG",
    "MW",
    "ML",
    "MR",
    "MU",
    "MA",
    "MZ",
    "NA",
    "NE",
    "NG",
    "CG",
    "RE",
    "RW",
    "SH",
    "ST",
    "SN",
    "SC",
    "SL",
    "SO",
    "ZA",
    "SS",
    "SD",
    "SZ",
    "TZ",
    "TG",
    "TN",
    "UG",
    "EH",
    "ZM",
    "ZW",
]

# Global list with a few excludes
exclude = ["CN", "IN", "ID", "RU", "VN", "IR"]
