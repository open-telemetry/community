
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
    approvers = ["cijothomas", "reyang", "vishweshbankwar"]
    maintainers = ["CodeBlanch", "alanwest", "utpilla"]
}

module "python_sig" {
    source = "./modules/sig"
    name = "python"
    triagers = []
    approvers = ["aabmass", "ashu658", "jeremydvoss", "owais", "oxeye-nikolay", "pmcollins", "sanketmehta28", "shalevr", "srikanthccv"]
    maintainers = ["lzchen", "ocelotl"]
}

module "erlang_sig" {
    source = "./modules/sig"
    name = "erlang"
    triagers = []
    approvers = ["GregMefford", "ferd", "zachdaniel"]
    maintainers = ["bryannaegele", "deadtrickster", "hauleth", "tsloughter"]
}

module "collector_sig" {
    source = "./modules/sig"
    name = "collector"
    triagers = ["astencel-sumo", "atoulme", "songy23"]
    approvers = ["Aneurysm9", "djaglowski", "jpkrohling"]
    maintainers = ["bogdandrutu", "codeboten", "dmitryax", "mx-psi"]
}

module "docs_sig" {
    source = "./modules/sig"
    name = "docs"
    triagers = []
    approvers = ["paulsbruce", "tedsuo"]
    maintainers = ["austinlparker", "cartermp", "chalin", "flands", "jparsana", "mtwo", "svrnm"]
}

module "javascript_sig" {
    source = "./modules/sig"
    name = "javascript"
    triagers = []
    approvers = ["Flarna", "JamieDanielson", "MSNev", "haddasbronfman", "hectorhdzg", "martinkuba", "mwear", "naseemkullah", "pkanal", "svetlanabrennan", "trentm"]
    maintainers = ["blumamir", "dyladan", "legendecas", "pichlermarc"]
}

module "java_sig" {
    source = "./modules/sig"
    name = "java"
    triagers = []
    approvers = ["breedx-splk", "jsuereth", "mateuszrzeszutek", "trask"]
    maintainers = ["jack-berg", "jkwatson"]
}

module "go_sig" {
    source = "./modules/sig"
    name = "go"
    triagers = ["alolita"]
    approvers = ["Aneurysm9", "XSAM", "dashpole", "dmathieu", "evantorrie", "hanyuancheung"]
    maintainers = ["MadVikingGod", "MrAlias", "pellared"]
}

module "technical-committee_wg" {
    source = "./modules/wg"
    name = "technical-committee"
    members = ["arminru", "bogdandrutu", "carlosalberto", "jack-berg", "jmacd", "jsuereth", "reyang", "tigrannajaryan", "yurishkuro"]
}

module "specs_sig" {
    source = "./modules/sig"
    name = "specs"
    triagers = ["andrewhsu", "rbailey7210"]
    approvers = ["arminru", "bogdandrutu", "carlosalberto", "jack-berg", "jmacd", "jsuereth", "reyang", "tigrannajaryan", "yurishkuro"]
    maintainers = []
}

module "ruby_sig" {
    source = "./modules/sig"
    name = "ruby"
    triagers = []
    approvers = ["ahayworth", "arielvalentin", "ericmustin", "plantfansam", "robbkidd"]
    maintainers = ["dazuma", "fbogsany", "mwear", "robertlaurin"]
}

module "cpp_sig" {
    source = "./modules/sig"
    name = "cpp"
    triagers = []
    approvers = ["jsuereth", "owent"]
    maintainers = ["ThomsonTan", "esigo", "lalitb", "marcalff"]
}

module "docs-cn_sig" {
    source = "./modules/sig"
    name = "docs-cn"
    triagers = []
    approvers = ["addname", "tydhot"]
    maintainers = ["laziobird", "sunface", "tensorchen"]
}

module "php_sig" {
    source = "./modules/sig"
    name = "php"
    triagers = ["jodeev"]
    approvers = ["Fahmy-Mohammed", "beniamin", "kishannsangani", "morrisonlevi", "zsistla"]
    maintainers = ["bobstrecansky", "brettmc", "pdelewski", "tidal"]
}

module "java-instrumentation_sig" {
    source = "./modules/sig"
    name = "java-instrumentation"
    triagers = []
    approvers = ["breedx-splk", "jack-berg", "jkwatson"]
    maintainers = ["laurit", "mateuszrzeszutek", "trask"]
}

module "opentelemetry-python-contrib_sig" {
    source = "./modules/sig"
    name = "opentelemetry-python-contrib"
    triagers = []
    approvers = ["NathanielRN", "aabmass", "ashu658", "jeremydvoss", "nikosokolik", "owais", "oxeye-nikolay", "pmcollins", "sanketmehta28", "srikanthccv"]
    maintainers = ["lzchen", "ocelotl", "shalevr"]
}

module "rust_sig" {
    source = "./modules/sig"
    name = "rust"
    triagers = []
    approvers = ["MikeGoldsmith", "awiede", "frigus02", "iredelmeier", "lalitb", "shaun-cox"]
    maintainers = ["TommyCpp", "cijothomas", "hdost", "jtescher"]
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
    triagers = ["Frapschen", "JaredTan95", "bryan-aguilar", "crobert-1", "frzifus", "gbbr", "gouthamve", "mwear"]
    approvers = ["Aneurysm9", "MovieStoreGuy", "TylerHelmuth", "astencel-sumo", "atoulme", "bogdandrutu", "codeboten", "dashpole", "djaglowski", "dmitryax", "evan-bradley", "fatsheep9146", "jpkrohling", "mx-psi", "songy23"]
    maintainers = []
}

module "collector-contrib-maintainer_wg" {
    source = "./modules/wg"
    name = "collector-contrib-maintainer"
    members = ["MovieStoreGuy", "TylerHelmuth", "bogdandrutu", "codeboten", "djaglowski", "dmitryax", "evan-bradley", "jpkrohling", "mx-psi"]
}

module "specs-trace_sig" {
    source = "./modules/sig"
    name = "specs-trace"
    triagers = []
    approvers = ["Oberon00", "iNikem", "tedsuo"]
    maintainers = []
}

module "specs-metrics_sig" {
    source = "./modules/sig"
    name = "specs-metrics"
    triagers = []
    approvers = ["MrAlias", "cijothomas", "lzchen"]
    maintainers = []
}

module "specs-logs_sig" {
    source = "./modules/sig"
    name = "specs-logs"
    triagers = []
    approvers = ["djaglowski", "kumoroku", "zenmoto"]
    maintainers = []
}

module "dotnet-instrumentation_sig" {
    source = "./modules/sig"
    name = "dotnet-instrumentation"
    triagers = ["MikeGoldsmith", "elucus"]
    approvers = ["RassK", "cijothomas", "macrogreg"]
    maintainers = ["Kielek", "nrcventura", "pellared", "pjanotti", "rajkumar-rangaraj", "zacharycmontoya"]
}

module "governance-committee_wg" {
    source = "./modules/wg"
    name = "governance-committee"
    members = ["alolita", "austinlparker", "danielgblanco", "dyladan", "jpkrohling", "mtwo", "svrnm", "tedsuo", "trask"]
}

module "java-contrib_sig" {
    source = "./modules/sig"
    name = "java-contrib"
    triagers = ["Mrod1598", "PeterF778", "anosek-an", "breedx-splk", "cyrille-leclerc", "dehaansa", "iNikem", "kenfinnigan", "kittylyst", "oertl", "willarmiros"]
    approvers = ["laurit"]
    maintainers = ["jack-berg", "mateuszrzeszutek", "trask"]
}

module "helm_sig" {
    source = "./modules/sig"
    name = "helm"
    triagers = ["naseemkullah", "tigrannajaryan"]
    approvers = ["Allex1", "povilasv", "puckpuck"]
    maintainers = ["TylerHelmuth", "dmitryax"]
}

module "lambda-extension_sig" {
    source = "./modules/sig"
    name = "lambda-extension"
    triagers = []
    approvers = ["tsloughter"]
    maintainers = ["rapphil", "tylerbenson"]
}

module "wg-prometheus_wg" {
    source = "./modules/wg"
    name = "wg-prometheus"
    members = ["Aneurysm9", "alolita", "dashpole", "jsuereth", "punya", "rakyll"]
}

module "dotnet-contrib_sig" {
    source = "./modules/sig"
    name = "dotnet-contrib"
    triagers = []
    approvers = []
    maintainers = ["CodeBlanch", "Kielek", "alanwest", "cijothomas", "utpilla"]
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
    approvers = ["DebajitDas", "ThomsonTan", "TomRoSystems", "esigo", "jsuereth", "kpratyus", "marcalff", "maxgolov", "pyohannes", "seemk", "tobiasstadler"]
    maintainers = ["lalitb"]
}

module "proto-go_sig" {
    source = "./modules/sig"
    name = "proto-go"
    triagers = []
    approvers = ["Aneurysm9", "MadVikingGod", "pellared"]
    maintainers = ["MikeGoldsmith", "MrAlias"]
}

module "erlang-contrib_sig" {
    source = "./modules/sig"
    name = "erlang-contrib"
    triagers = []
    approvers = ["GregMefford", "deadtrickster", "ferd", "hauleth", "zachdaniel"]
    maintainers = ["bryannaegele", "tsloughter"]
}

module "assign-reviewers-action_sig" {
    source = "./modules/sig"
    name = "assign-reviewers-action"
    triagers = []
    approvers = []
    maintainers = ["dyladan", "trask"]
}

module "otel-elections_wg" {
    source = "./modules/wg"
    name = "otel-elections"
    members = ["dyladan", "mtwo", "trask"]
}

module "sqlcommenter_sig" {
    source = "./modules/sig"
    name = "sqlcommenter"
    triagers = []
    approvers = ["alolita", "jsuereth", "weyert"]
    maintainers = ["aabmass", "sjs994", "srikanthccv"]
}

module "opamp-go_sig" {
    source = "./modules/sig"
    name = "opamp-go"
    triagers = []
    approvers = ["Aneurysm9", "codeboten", "djaglowski", "srikanthccv"]
    maintainers = ["andykellr", "tigrannajaryan"]
}

module "opamp-spec_sig" {
    source = "./modules/sig"
    name = "opamp-spec"
    triagers = []
    approvers = ["andykellr", "codeboten", "djaglowski"]
    maintainers = ["tigrannajaryan"]
}

module "instr-wg_wg" {
    source = "./modules/wg"
    name = "instr-wg"
    members = ["MovieStoreGuy", "arminru", "denisivan0v", "dpauls", "jamesmoessis", "joaopgrassi", "kenfinnigan", "lmolkova", "pyohannes", "tedsuo", "tigrannajaryan", "trask"]
}

module "blog_sig" {
    source = "./modules/sig"
    name = "blog"
    triagers = []
    approvers = ["SergeyKanzhelev", "alolita", "austinlparker", "cartermp", "mtwo", "svrnm"]
    maintainers = []
}

module "ruby-contrib_sig" {
    source = "./modules/sig"
    name = "ruby-contrib"
    triagers = []
    approvers = ["kaylareopelle", "simi"]
    maintainers = ["ahayworth", "arielvalentin", "dazuma", "ericmustin", "fbogsany", "mwear", "plantfansam", "robbkidd", "robertlaurin"]
}

module "demo_sig" {
    source = "./modules/sig"
    name = "demo"
    triagers = []
    approvers = ["cedricziel", "fatsheep9146", "mviitane", "reyang", "wph95"]
    maintainers = ["austinlparker", "cartersocha", "julianocosta89", "puckpuck"]
}

module "sandbox-web-js_sig" {
    source = "./modules/sig"
    name = "sandbox-web-js"
    triagers = []
    approvers = []
    maintainers = ["MSNev", "dyladan", "martinkuba", "tedsuo"]
}

module "go-instrumentation_sig" {
    source = "./modules/sig"
    name = "go-instrumentation"
    triagers = ["jmacd"]
    approvers = ["MadVikingGod", "RonFed", "damemi", "dineshg13", "pellared"]
    maintainers = ["MikeGoldsmith", "MrAlias", "edeNFed", "pdelewski"]
}

module "ebpf_sig" {
    source = "./modules/sig"
    name = "ebpf"
    triagers = ["atoulme"]
    approvers = ["samiura"]
    maintainers = ["bjandras", "jmw51798", "yonch"]
}

module "arrow_sig" {
    source = "./modules/sig"
    name = "arrow"
    triagers = []
    approvers = ["codeboten", "moh-osman3"]
    maintainers = ["jmacd", "lquerel"]
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
    members = ["avillela", "mhausenblas", "musingvirtual", "reese-lee", "sharrmander"]
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
    approvers = ["MovieStoreGuy", "Oberon00", "jamesmoessis", "lmolkova", "pyohannes", "tedsuo"]
    maintainers = ["AlexanderWert", "arminru", "joaopgrassi", "jsuereth", "reyang"]
}

module "configuration_sig" {
    source = "./modules/sig"
    name = "configuration"
    triagers = []
    approvers = []
    maintainers = ["MrAlias", "codeboten", "jack-berg", "tsloughter"]
}

module "semconv-http_sig" {
    source = "./modules/sig"
    name = "semconv-http"
    triagers = []
    approvers = ["lmolkova", "trask"]
    maintainers = []
}

module "semconv-jvm_sig" {
    source = "./modules/sig"
    name = "semconv-jvm"
    triagers = []
    approvers = ["jack-berg", "jonatan-ivanov", "mateuszrzeszutek", "trask"]
    maintainers = []
}

module "sig-security_sig" {
    source = "./modules/sig"
    name = "sig-security"
    triagers = []
    approvers = []
    maintainers = ["cartersocha", "codeboten", "jpkrohling", "reyang"]
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
    approvers = ["ChrsMark", "dmitryax", "frzifus", "mx-psi"]
    maintainers = []
}

module "semconv-mobile_sig" {
    source = "./modules/sig"
    name = "semconv-mobile"
    triagers = []
    approvers = ["LikeTheSalad", "breedx-splk", "bryce-b", "nachoBonafonte", "surbhiia"]
    maintainers = []
}

module "semconv-dotnet-approver_wg" {
    source = "./modules/wg"
    name = "semconv-dotnet-approver"
    members = ["JamesNK", "antonfirsov", "noahfalk"]
}

module "semconv-container_sig" {
    source = "./modules/sig"
    name = "semconv-container"
    triagers = []
    approvers = ["ChrsMark", "TylerHelmuth", "dmitryax", "frzifus", "jinja2", "mx-psi"]
    maintainers = []
}

module "semconv-k8s_sig" {
    source = "./modules/sig"
    name = "semconv-k8s"
    triagers = []
    approvers = ["ChrsMark", "TylerHelmuth", "dashpole", "dmitryax", "frzifus", "jinja2", "mx-psi"]
    maintainers = []
}

module "operator_sig" {
    source = "./modules/sig"
    name = "operator"
    triagers = []
    approvers = ["TylerHelmuth", "dmitryax", "frzifus", "swiatekm-sumo", "yuriolisa"]
    maintainers = ["VineethReddy02", "jaronoff97", "jpkrohling", "pavolloffay"]
}

module "operator-ta_sig" {
    source = "./modules/sig"
    name = "operator-ta"
    triagers = []
    approvers = []
    maintainers = ["Aneurysm9", "VineethReddy02", "jaronoff97", "jpkrohling", "kristinapathak", "pavolloffay", "secustor"]
}
