
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
    approvers = ["reyang", "vishweshbankwar", "cijothomas"]
    maintainers = ["alanwest", "utpilla", "CodeBlanch"]
}

module "python_sig" {
    source = "./modules/sig"
    name = "python"
    triagers = []
    approvers = ["jeremydvoss", "ashu658", "shalevr", "owais", "oxeye-nikolay", "sanketmehta28", "srikanthccv", "aabmass", "pmcollins"]
    maintainers = ["lzchen", "ocelotl"]
}

module "erlang_sig" {
    source = "./modules/sig"
    name = "erlang"
    triagers = []
    approvers = ["zachdaniel", "ferd", "GregMefford"]
    maintainers = ["deadtrickster", "tsloughter", "bryannaegele", "hauleth"]
}

module "collector_sig" {
    source = "./modules/sig"
    name = "collector"
    triagers = ["astencel-sumo", "songy23", "atoulme"]
    approvers = ["Aneurysm9", "djaglowski", "jpkrohling"]
    maintainers = ["codeboten", "mx-psi", "dmitryax", "bogdandrutu"]
}

module "docs_sig" {
    source = "./modules/sig"
    name = "docs"
    triagers = []
    approvers = ["tedsuo", "paulsbruce"]
    maintainers = ["mtwo", "cartermp", "flands", "svrnm", "jparsana", "austinlparker", "chalin"]
}

module "javascript_sig" {
    source = "./modules/sig"
    name = "javascript"
    triagers = []
    approvers = ["martinkuba", "MSNev", "trentm", "svetlanabrennan", "naseemkullah", "mwear", "pkanal", "haddasbronfman", "hectorhdzg", "Flarna", "JamieDanielson"]
    maintainers = ["pichlermarc", "blumamir", "legendecas", "dyladan"]
}

module "java_sig" {
    source = "./modules/sig"
    name = "java"
    triagers = []
    approvers = ["breedx-splk", "mateuszrzeszutek", "trask", "jsuereth"]
    maintainers = ["jkwatson", "jack-berg"]
}

module "go_sig" {
    source = "./modules/sig"
    name = "go"
    triagers = ["alolita"]
    approvers = ["dmathieu", "hanyuancheung", "evantorrie", "XSAM", "dashpole", "Aneurysm9"]
    maintainers = ["MrAlias", "MadVikingGod", "pellared"]
}

module "technical-committee_wg" {
    source = "./modules/wg"
    name = "technical-committee"
    members = ["jmacd", "carlosalberto", "yurishkuro", "arminru", "reyang", "jsuereth", "bogdandrutu", "tigrannajaryan", "jack-berg"]
}

module "specs_sig" {
    source = "./modules/sig"
    name = "specs"
    triagers = ["rbailey7210", "andrewhsu"]
    approvers = ["jmacd", "carlosalberto", "yurishkuro", "arminru", "reyang", "jsuereth", "bogdandrutu", "tigrannajaryan", "jack-berg"]
    maintainers = []
}

module "ruby_sig" {
    source = "./modules/sig"
    name = "ruby"
    triagers = []
    approvers = ["arielvalentin", "ahayworth", "plantfansam", "ericmustin", "robbkidd"]
    maintainers = ["robertlaurin", "mwear", "fbogsany", "dazuma"]
}

module "cpp_sig" {
    source = "./modules/sig"
    name = "cpp"
    triagers = []
    approvers = ["owent", "jsuereth"]
    maintainers = ["lalitb", "marcalff", "esigo", "ThomsonTan"]
}

module "docs-cn_sig" {
    source = "./modules/sig"
    name = "docs-cn"
    triagers = []
    approvers = ["tydhot", "addname"]
    maintainers = ["laziobird", "sunface", "tensorchen"]
}

module "php_sig" {
    source = "./modules/sig"
    name = "php"
    triagers = ["jodeev"]
    approvers = ["kishannsangani", "zsistla", "morrisonlevi", "Fahmy-Mohammed", "beniamin"]
    maintainers = ["pdelewski", "tidal", "bobstrecansky", "brettmc"]
}

module "java-instrumentation_sig" {
    source = "./modules/sig"
    name = "java-instrumentation"
    triagers = []
    approvers = ["jkwatson", "breedx-splk", "jack-berg"]
    maintainers = ["mateuszrzeszutek", "laurit", "trask"]
}

module "opentelemetry-python-contrib_sig" {
    source = "./modules/sig"
    name = "opentelemetry-python-contrib"
    triagers = []
    approvers = ["jeremydvoss", "ashu658", "nikosokolik", "owais", "oxeye-nikolay", "sanketmehta28", "srikanthccv", "NathanielRN", "aabmass", "pmcollins"]
    maintainers = ["lzchen", "shalevr", "ocelotl"]
}

module "rust_sig" {
    source = "./modules/sig"
    name = "rust"
    triagers = []
    approvers = ["frigus02", "awiede", "lalitb", "MikeGoldsmith", "iredelmeier", "shaun-cox"]
    maintainers = ["TommyCpp", "hdost", "jtescher", "cijothomas"]
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
    triagers = ["Frapschen", "bryan-aguilar", "mwear", "crobert-1", "JaredTan95", "gbbr", "gouthamve", "frzifus"]
    approvers = ["codeboten", "djaglowski", "jpkrohling", "mx-psi", "evan-bradley", "TylerHelmuth", "dmitryax", "dashpole", "Aneurysm9", "bogdandrutu", "fatsheep9146", "MovieStoreGuy", "songy23", "astencel-sumo", "atoulme"]
    maintainers = []
}

module "collector-contrib-maintainer_wg" {
    source = "./modules/wg"
    name = "collector-contrib-maintainer"
    members = ["djaglowski", "codeboten", "jpkrohling", "mx-psi", "evan-bradley", "TylerHelmuth", "dmitryax", "bogdandrutu", "MovieStoreGuy"]
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
    approvers = ["MrAlias", "lzchen", "cijothomas"]
    maintainers = []
}

module "specs-logs_sig" {
    source = "./modules/sig"
    name = "specs-logs"
    triagers = []
    approvers = ["djaglowski", "zenmoto", "kumoroku"]
    maintainers = []
}

module "dotnet-instrumentation_sig" {
    source = "./modules/sig"
    name = "dotnet-instrumentation"
    triagers = ["MikeGoldsmith", "elucus"]
    approvers = ["macrogreg", "RassK", "cijothomas"]
    maintainers = ["zacharycmontoya", "rajkumar-rangaraj", "nrcventura", "pellared", "pjanotti", "Kielek"]
}

module "governance-committee_wg" {
    source = "./modules/wg"
    name = "governance-committee"
    members = ["jpkrohling", "mtwo", "alolita", "danielgblanco", "svrnm", "dyladan", "tedsuo", "austinlparker", "trask"]
}

module "java-contrib_sig" {
    source = "./modules/sig"
    name = "java-contrib"
    triagers = ["Mrod1598", "breedx-splk", "willarmiros", "dehaansa", "PeterF778", "iNikem", "oertl", "kenfinnigan", "cyrille-leclerc", "kittylyst", "anosek-an"]
    approvers = ["laurit"]
    maintainers = ["mateuszrzeszutek", "trask", "jack-berg"]
}

module "helm_sig" {
    source = "./modules/sig"
    name = "helm"
    triagers = ["naseemkullah", "tigrannajaryan"]
    approvers = ["povilasv", "puckpuck", "Allex1"]
    maintainers = ["TylerHelmuth", "dmitryax"]
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
    members = ["rakyll", "alolita", "jsuereth", "dashpole", "Aneurysm9", "punya"]
}

module "dotnet-contrib_sig" {
    source = "./modules/sig"
    name = "dotnet-contrib"
    triagers = []
    approvers = []
    maintainers = ["CodeBlanch", "cijothomas", "alanwest", "utpilla", "Kielek"]
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
    approvers = ["marcalff", "seemk", "esigo", "tobiasstadler", "ThomsonTan", "TomRoSystems", "jsuereth", "kpratyus", "maxgolov", "DebajitDas", "pyohannes"]
    maintainers = ["lalitb"]
}

module "proto-go_sig" {
    source = "./modules/sig"
    name = "proto-go"
    triagers = []
    approvers = ["Aneurysm9", "MadVikingGod", "pellared"]
    maintainers = ["MrAlias", "MikeGoldsmith"]
}

module "erlang-contrib_sig" {
    source = "./modules/sig"
    name = "erlang-contrib"
    triagers = []
    approvers = ["deadtrickster", "zachdaniel", "hauleth", "ferd", "GregMefford"]
    maintainers = ["tsloughter", "bryannaegele"]
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
    approvers = ["andykellr", "djaglowski", "codeboten"]
    maintainers = ["tigrannajaryan"]
}

module "instr-wg_wg" {
    source = "./modules/wg"
    name = "instr-wg"
    members = ["jamesmoessis", "denisivan0v", "lmolkova", "arminru", "MovieStoreGuy", "kenfinnigan", "pyohannes", "tedsuo", "joaopgrassi", "tigrannajaryan", "trask", "dpauls"]
}

module "blog_sig" {
    source = "./modules/sig"
    name = "blog"
    triagers = []
    approvers = ["mtwo", "cartermp", "svrnm", "SergeyKanzhelev", "alolita", "austinlparker"]
    maintainers = []
}

module "ruby-contrib_sig" {
    source = "./modules/sig"
    name = "ruby-contrib"
    triagers = []
    approvers = ["kaylareopelle", "simi"]
    maintainers = ["arielvalentin", "dazuma", "ahayworth", "mwear", "plantfansam", "ericmustin", "fbogsany", "robertlaurin", "robbkidd"]
}

module "demo_sig" {
    source = "./modules/sig"
    name = "demo"
    triagers = []
    approvers = ["wph95", "reyang", "mviitane", "fatsheep9146", "cedricziel"]
    maintainers = ["austinlparker", "puckpuck", "cartersocha", "julianocosta89"]
}

module "sandbox-web-js_sig" {
    source = "./modules/sig"
    name = "sandbox-web-js"
    triagers = []
    approvers = []
    maintainers = ["martinkuba", "tedsuo", "MSNev", "dyladan"]
}

module "go-instrumentation_sig" {
    source = "./modules/sig"
    name = "go-instrumentation"
    triagers = ["jmacd"]
    approvers = ["MadVikingGod", "RonFed", "damemi", "dineshg13", "pellared"]
    maintainers = ["MrAlias", "MikeGoldsmith", "pdelewski", "edeNFed"]
}

module "ebpf_sig" {
    source = "./modules/sig"
    name = "ebpf"
    triagers = ["atoulme"]
    approvers = ["samiura"]
    maintainers = ["yonch", "bjandras", "jmw51798"]
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
    members = ["reese-lee", "avillela", "musingvirtual", "sharrmander", "mhausenblas"]
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
    approvers = ["jamesmoessis", "Oberon00", "lmolkova", "MovieStoreGuy", "tedsuo", "pyohannes"]
    maintainers = ["AlexanderWert", "reyang", "arminru", "jsuereth", "joaopgrassi"]
}

module "configuration_sig" {
    source = "./modules/sig"
    name = "configuration"
    triagers = []
    approvers = []
    maintainers = ["MrAlias", "tsloughter", "codeboten", "jack-berg"]
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
    approvers = ["jonatan-ivanov", "mateuszrzeszutek", "trask", "jack-berg"]
    maintainers = []
}

module "sig-security_sig" {
    source = "./modules/sig"
    name = "sig-security"
    triagers = []
    approvers = []
    maintainers = ["codeboten", "reyang", "jpkrohling", "cartersocha"]
}

module "android_sig" {
    source = "./modules/sig"
    name = "android"
    triagers = []
    approvers = ["trask", "jack-berg"]
    maintainers = ["LikeTheSalad", "breedx-splk"]
}

module "semconv-system_sig" {
    source = "./modules/sig"
    name = "semconv-system"
    triagers = []
    approvers = ["ChrsMark", "mx-psi", "dmitryax", "frzifus"]
    maintainers = []
}

module "semconv-mobile_sig" {
    source = "./modules/sig"
    name = "semconv-mobile"
    triagers = []
    approvers = ["LikeTheSalad", "bryce-b", "nachoBonafonte", "breedx-splk", "surbhiia"]
    maintainers = []
}

module "semconv-dotnet-approver_wg" {
    source = "./modules/wg"
    name = "semconv-dotnet-approver"
    members = ["antonfirsov", "JamesNK", "noahfalk"]
}

module "semconv-container_sig" {
    source = "./modules/sig"
    name = "semconv-container"
    triagers = []
    approvers = ["mx-psi", "ChrsMark", "jinja2", "TylerHelmuth", "dmitryax", "frzifus"]
    maintainers = []
}

module "semconv-k8s_sig" {
    source = "./modules/sig"
    name = "semconv-k8s"
    triagers = []
    approvers = ["mx-psi", "ChrsMark", "jinja2", "TylerHelmuth", "dmitryax", "frzifus", "dashpole"]
    maintainers = []
}

module "operator_sig" {
    source = "./modules/sig"
    name = "operator"
    triagers = []
    approvers = ["TylerHelmuth", "swiatekm-sumo", "dmitryax", "yuriolisa", "frzifus"]
    maintainers = ["pavolloffay", "VineethReddy02", "jaronoff97", "jpkrohling"]
}

module "operator-ta_sig" {
    source = "./modules/sig"
    name = "operator-ta"
    triagers = []
    approvers = []
    maintainers = ["jpkrohling", "pavolloffay", "kristinapathak", "Aneurysm9", "VineethReddy02", "secustor", "jaronoff97"]
}
