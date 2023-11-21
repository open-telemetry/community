
module "memberships" {
  for_each = toset(var.members)
  source   = "./modules/member"
  username = each.key
  role     = "member"
}

module "owners" {
  for_each = toset(var.owners)
  source   = "./modules/member"
  username = each.key
  role     = "admin"
}

module "dotnet_sig" {
    source = "./modules/sig"
    name = "dotnet"
    triagers = []
    approvers = ["cijothomas", "vishweshbankwar", "reyang"]
    maintainers = ["alanwest", "CodeBlanch", "utpilla"]
}

module "python_sig" {
    source = "./modules/sig"
    name = "python"
    triagers = []
    approvers = ["ashu658", "shalevr", "aabmass", "oxeye-nikolay", "sanketmehta28", "owais", "jeremydvoss", "pmcollins", "srikanthccv"]
    maintainers = ["lzchen", "ocelotl"]
}

module "erlang_sig" {
    source = "./modules/sig"
    name = "erlang"
    triagers = []
    approvers = ["zachdaniel", "GregMefford", "ferd"]
    maintainers = ["bryannaegele", "tsloughter", "deadtrickster", "hauleth"]
}

module "collector_sig" {
    source = "./modules/sig"
    name = "collector"
    triagers = ["songy23", "atoulme", "astencel-sumo"]
    approvers = ["jpkrohling", "djaglowski", "Aneurysm9"]
    maintainers = ["dmitryax", "bogdandrutu", "codeboten", "mx-psi"]
}

module "docs_sig" {
    source = "./modules/sig"
    name = "docs"
    triagers = []
    approvers = ["tedsuo", "paulsbruce"]
    maintainers = ["svrnm", "austinlparker", "jparsana", "cartermp", "chalin", "mtwo", "flands"]
}

module "javascript_sig" {
    source = "./modules/sig"
    name = "javascript"
    triagers = []
    approvers = ["trentm", "pkanal", "Flarna", "JamieDanielson", "naseemkullah", "martinkuba", "svetlanabrennan", "haddasbronfman", "mwear", "hectorhdzg", "MSNev"]
    maintainers = ["legendecas", "blumamir", "pichlermarc", "dyladan"]
}

module "java_sig" {
    source = "./modules/sig"
    name = "java"
    triagers = []
    approvers = ["mateuszrzeszutek", "trask", "breedx-splk", "jsuereth"]
    maintainers = ["jack-berg", "jkwatson"]
}

module "go_sig" {
    source = "./modules/sig"
    name = "go"
    triagers = ["alolita"]
    approvers = ["hanyuancheung", "dashpole", "Aneurysm9", "evantorrie", "XSAM", "dmathieu"]
    maintainers = ["MrAlias", "MadVikingGod", "pellared"]
}

module "technical-committee_wg" {
    source = "./modules/wg"
    name = "technical-committee"
    members = ["jack-berg", "arminru", "jsuereth", "bogdandrutu", "carlosalberto", "tigrannajaryan", "reyang", "jmacd", "yurishkuro"]
}

module "specs_sig" {
    source = "./modules/sig"
    name = "specs"
    triagers = ["andrewhsu", "rbailey7210"]
    approvers = ["jack-berg", "arminru", "jsuereth", "bogdandrutu", "carlosalberto", "tigrannajaryan", "reyang", "jmacd", "yurishkuro"]
    maintainers = []
}

module "ruby_sig" {
    source = "./modules/sig"
    name = "ruby"
    triagers = []
    approvers = ["ahayworth", "robbkidd", "plantfansam", "arielvalentin", "ericmustin"]
    maintainers = ["dazuma", "robertlaurin", "mwear", "fbogsany"]
}

module "cpp_sig" {
    source = "./modules/sig"
    name = "cpp"
    triagers = []
    approvers = ["owent", "jsuereth"]
    maintainers = ["ThomsonTan", "marcalff", "esigo", "lalitb"]
}

module "docs-cn_sig" {
    source = "./modules/sig"
    name = "docs-cn"
    triagers = []
    approvers = ["tydhot", "addname"]
    maintainers = ["sunface", "tensorchen", "laziobird"]
}

module "php_sig" {
    source = "./modules/sig"
    name = "php"
    triagers = ["jodeev"]
    approvers = ["kishannsangani", "Fahmy-Mohammed", "beniamin", "zsistla", "morrisonlevi"]
    maintainers = ["bobstrecansky", "brettmc", "pdelewski", "tidal"]
}

module "java-instrumentation_sig" {
    source = "./modules/sig"
    name = "java-instrumentation"
    triagers = []
    approvers = ["jack-berg", "breedx-splk", "jkwatson"]
    maintainers = ["laurit", "trask", "mateuszrzeszutek"]
}

module "opentelemetry-python-contrib_sig" {
    source = "./modules/sig"
    name = "opentelemetry-python-contrib"
    triagers = []
    approvers = ["ashu658", "aabmass", "oxeye-nikolay", "sanketmehta28", "owais", "NathanielRN", "jeremydvoss", "pmcollins", "srikanthccv", "nikosokolik"]
    maintainers = ["lzchen", "ocelotl", "shalevr"]
}

module "rust_sig" {
    source = "./modules/sig"
    name = "rust"
    triagers = []
    approvers = ["frigus02", "lalitb", "iredelmeier", "shaun-cox", "awiede", "MikeGoldsmith"]
    maintainers = ["cijothomas", "jtescher", "TommyCpp", "hdost"]
}

module "swift_sig" {
    source = "./modules/sig"
    name = "swift"
    triagers = []
    approvers = ["vvydier"]
    maintainers = ["bryce-b", "nachoBonafonte"]
}

module "collector-contrib_sig" {
    source = "./modules/sig"
    name = "collector-contrib"
    triagers = ["gouthamve", "Frapschen", "bryan-aguilar", "JaredTan95", "frzifus", "mwear", "crobert-1", "gbbr"]
    approvers = ["djaglowski", "songy23", "bogdandrutu", "jpkrohling", "dashpole", "Aneurysm9", "evan-bradley", "MovieStoreGuy", "fatsheep9146", "TylerHelmuth", "astencel-sumo", "atoulme", "dmitryax", "codeboten", "mx-psi"]
    maintainers = []
}

module "collector-contrib-maintainer_wg" {
    source = "./modules/wg"
    name = "collector-contrib-maintainer"
    members = ["djaglowski", "jpkrohling", "bogdandrutu", "evan-bradley", "MovieStoreGuy", "TylerHelmuth", "dmitryax", "codeboten", "mx-psi"]
}

module "specs-trace_sig" {
    source = "./modules/sig"
    name = "specs-trace"
    triagers = []
    approvers = ["tedsuo", "Oberon00", "iNikem"]
    maintainers = []
}

module "specs-metrics_sig" {
    source = "./modules/sig"
    name = "specs-metrics"
    triagers = []
    approvers = ["cijothomas", "lzchen", "MrAlias"]
    maintainers = []
}

module "specs-logs_sig" {
    source = "./modules/sig"
    name = "specs-logs"
    triagers = []
    approvers = ["kumoroku", "djaglowski", "zenmoto"]
    maintainers = []
}

module "dotnet-instrumentation_sig" {
    source = "./modules/sig"
    name = "dotnet-instrumentation"
    triagers = ["elucus", "MikeGoldsmith"]
    approvers = ["cijothomas", "RassK", "macrogreg"]
    maintainers = ["Kielek", "pjanotti", "rajkumar-rangaraj", "zacharycmontoya", "pellared", "nrcventura"]
}

module "governance-committee_wg" {
    source = "./modules/wg"
    name = "governance-committee"
    members = ["svrnm", "trask", "austinlparker", "danielgblanco", "jpkrohling", "mtwo", "tedsuo", "alolita", "dyladan"]
}

module "java-contrib_sig" {
    source = "./modules/sig"
    name = "java-contrib"
    triagers = ["iNikem", "kenfinnigan", "PeterF778", "Mrod1598", "oertl", "willarmiros", "anosek-an", "cyrille-leclerc", "breedx-splk", "dehaansa", "kittylyst"]
    approvers = ["laurit"]
    maintainers = ["jack-berg", "trask", "mateuszrzeszutek"]
}

module "helm_sig" {
    source = "./modules/sig"
    name = "helm"
    triagers = ["naseemkullah", "tigrannajaryan"]
    approvers = ["povilasv", "puckpuck", "Allex1"]
    maintainers = ["dmitryax", "TylerHelmuth"]
}

module "lambda-extension_sig" {
    source = "./modules/sig"
    name = "lambda-extension"
    triagers = []
    approvers = ["tsloughter"]
    maintainers = ["tylerbenson", "rapphil"]
}

module "wg-prometheus_wg" {
    source = "./modules/wg"
    name = "wg-prometheus"
    members = ["punya", "jsuereth", "dashpole", "Aneurysm9", "alolita", "rakyll"]
}

module "dotnet-contrib_sig" {
    source = "./modules/sig"
    name = "dotnet-contrib"
    triagers = []
    approvers = []
    maintainers = ["Kielek", "utpilla", "CodeBlanch", "cijothomas", "alanwest"]
}

module "build-tools_sig" {
    source = "./modules/sig"
    name = "build-tools"
    triagers = []
    approvers = ["Oberon00"]
    maintainers = []
}

module "cpp-contrib_sig" {
    source = "./modules/sig"
    name = "cpp-contrib"
    triagers = []
    approvers = ["seemk", "marcalff", "DebajitDas", "jsuereth", "ThomsonTan", "TomRoSystems", "pyohannes", "maxgolov", "kpratyus", "tobiasstadler", "esigo"]
    maintainers = ["lalitb"]
}

module "proto-go_sig" {
    source = "./modules/sig"
    name = "proto-go"
    triagers = []
    approvers = ["MadVikingGod", "pellared", "Aneurysm9"]
    maintainers = ["MrAlias", "MikeGoldsmith"]
}

module "erlang-contrib_sig" {
    source = "./modules/sig"
    name = "erlang-contrib"
    triagers = []
    approvers = ["deadtrickster", "ferd", "zachdaniel", "GregMefford", "hauleth"]
    maintainers = ["tsloughter", "bryannaegele"]
}

module "assign-reviewers-action_sig" {
    source = "./modules/sig"
    name = "assign-reviewers-action"
    triagers = []
    approvers = []
    maintainers = ["trask", "dyladan"]
}

module "otel-elections_wg" {
    source = "./modules/wg"
    name = "otel-elections"
    members = ["trask", "dyladan", "mtwo"]
}

module "sqlcommenter_sig" {
    source = "./modules/sig"
    name = "sqlcommenter"
    triagers = []
    approvers = ["alolita", "weyert", "jsuereth"]
    maintainers = ["srikanthccv", "sjs994", "aabmass"]
}

module "opamp-go_sig" {
    source = "./modules/sig"
    name = "opamp-go"
    triagers = []
    approvers = ["srikanthccv", "djaglowski", "codeboten", "Aneurysm9"]
    maintainers = ["andykellr", "tigrannajaryan"]
}

module "opamp-spec_sig" {
    source = "./modules/sig"
    name = "opamp-spec"
    triagers = []
    approvers = ["codeboten", "djaglowski", "andykellr"]
    maintainers = ["tigrannajaryan"]
}

module "instr-wg_wg" {
    source = "./modules/wg"
    name = "instr-wg"
    members = ["jamesmoessis", "trask", "arminru", "lmolkova", "kenfinnigan", "denisivan0v", "dpauls", "tigrannajaryan", "pyohannes", "MovieStoreGuy", "tedsuo", "joaopgrassi"]
}

module "blog_sig" {
    source = "./modules/sig"
    name = "blog"
    triagers = []
    approvers = ["svrnm", "austinlparker", "alolita", "cartermp", "SergeyKanzhelev", "mtwo"]
    maintainers = []
}

module "ruby-contrib_sig" {
    source = "./modules/sig"
    name = "ruby-contrib"
    triagers = []
    approvers = ["simi", "kaylareopelle"]
    maintainers = ["ahayworth", "robbkidd", "robertlaurin", "fbogsany", "plantfansam", "mwear", "dazuma", "arielvalentin", "ericmustin"]
}

module "demo_sig" {
    source = "./modules/sig"
    name = "demo"
    triagers = []
    approvers = ["mviitane", "reyang", "fatsheep9146", "cedricziel", "wph95"]
    maintainers = ["julianocosta89", "austinlparker", "puckpuck", "cartersocha"]
}

module "sandbox-web-js_sig" {
    source = "./modules/sig"
    name = "sandbox-web-js"
    triagers = []
    approvers = []
    maintainers = ["tedsuo", "martinkuba", "dyladan", "MSNev"]
}

module "go-instrumentation_sig" {
    source = "./modules/sig"
    name = "go-instrumentation"
    triagers = ["jmacd"]
    approvers = ["MadVikingGod", "dineshg13", "pellared", "damemi", "RonFed"]
    maintainers = ["MrAlias", "edeNFed", "pdelewski", "MikeGoldsmith"]
}

module "ebpf_sig" {
    source = "./modules/sig"
    name = "ebpf"
    triagers = ["atoulme"]
    approvers = ["samiura"]
    maintainers = ["jmw51798", "yonch", "bjandras"]
}

module "arrow_sig" {
    source = "./modules/sig"
    name = "arrow"
    triagers = []
    approvers = ["moh-osman3", "codeboten"]
    maintainers = ["lquerel", "jmacd"]
}

module "opamp-java_sig" {
    source = "./modules/sig"
    name = "opamp-java"
    triagers = []
    approvers = []
    maintainers = ["tigrannajaryan"]
}

module "end-user-wg_wg" {
    source = "./modules/wg"
    name = "end-user-wg"
    members = ["sharrmander", "musingvirtual", "avillela", "mhausenblas", "reese-lee"]
}

module "profiling_sig" {
    source = "./modules/sig"
    name = "profiling"
    triagers = []
    approvers = []
    maintainers = ["tigrannajaryan"]
}

module "specs-semconv_sig" {
    source = "./modules/sig"
    name = "specs-semconv"
    triagers = []
    approvers = ["Oberon00", "jamesmoessis", "lmolkova", "MovieStoreGuy", "pyohannes", "tedsuo"]
    maintainers = ["arminru", "jsuereth", "AlexanderWert", "reyang", "joaopgrassi"]
}

module "configuration_sig" {
    source = "./modules/sig"
    name = "configuration"
    triagers = []
    approvers = []
    maintainers = ["MrAlias", "jack-berg", "tsloughter", "codeboten"]
}

module "semconv-http_sig" {
    source = "./modules/sig"
    name = "semconv-http"
    triagers = []
    approvers = ["trask", "lmolkova"]
    maintainers = []
}

module "semconv-jvm_sig" {
    source = "./modules/sig"
    name = "semconv-jvm"
    triagers = []
    approvers = ["jack-berg", "trask", "jonatan-ivanov", "mateuszrzeszutek"]
    maintainers = []
}

module "sig-security_sig" {
    source = "./modules/sig"
    name = "sig-security"
    triagers = []
    approvers = []
    maintainers = ["jpkrohling", "cartersocha", "codeboten", "reyang"]
}

module "android_sig" {
    source = "./modules/sig"
    name = "android"
    triagers = []
    approvers = ["jack-berg", "trask"]
    maintainers = ["LikeTheSalad", "breedx-splk"]
}

module "semconv-system_sig" {
    source = "./modules/sig"
    name = "semconv-system"
    triagers = []
    approvers = ["dmitryax", "frzifus", "ChrsMark", "mx-psi"]
    maintainers = []
}

module "semconv-mobile_sig" {
    source = "./modules/sig"
    name = "semconv-mobile"
    triagers = []
    approvers = ["surbhiia", "nachoBonafonte", "bryce-b", "LikeTheSalad", "breedx-splk"]
    maintainers = []
}

module "semconv-dotnet-approver_wg" {
    source = "./modules/wg"
    name = "semconv-dotnet-approver"
    members = ["JamesNK", "noahfalk", "antonfirsov"]
}

module "semconv-container_sig" {
    source = "./modules/sig"
    name = "semconv-container"
    triagers = []
    approvers = ["TylerHelmuth", "jinja2", "frzifus", "ChrsMark", "dmitryax", "mx-psi"]
    maintainers = []
}

module "semconv-k8s_sig" {
    source = "./modules/sig"
    name = "semconv-k8s"
    triagers = []
    approvers = ["TylerHelmuth", "jinja2", "frzifus", "ChrsMark", "dmitryax", "dashpole", "mx-psi"]
    maintainers = []
}

module "operator_sig" {
    source = "./modules/sig"
    name = "operator"
    triagers = []
    approvers = ["swiatekm-sumo", "yuriolisa", "TylerHelmuth", "frzifus", "dmitryax"]
    maintainers = ["pavolloffay", "VineethReddy02", "jpkrohling", "jaronoff97"]
}

module "operator-ta_sig" {
    source = "./modules/sig"
    name = "operator-ta"
    triagers = []
    approvers = []
    maintainers = ["jpkrohling", "jaronoff97", "Aneurysm9", "pavolloffay", "secustor", "kristinapathak", "VineethReddy02"]
}
