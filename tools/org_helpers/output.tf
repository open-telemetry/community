
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
    approvers = ["sanketmehta28", "ashu658", "shalevr", "oxeye-nikolay", "owais", "aabmass", "pmcollins", "jeremydvoss", "srikanthccv"]
    maintainers = ["lzchen", "ocelotl"]
}

module "erlang_sig" {
    source = "./modules/sig"
    name = "erlang"
    triagers = []
    approvers = ["zachdaniel", "GregMefford", "ferd"]
    maintainers = ["hauleth", "deadtrickster", "tsloughter", "bryannaegele"]
}

module "collector_sig" {
    source = "./modules/sig"
    name = "collector"
    triagers = ["astencel-sumo", "atoulme", "songy23"]
    approvers = ["Aneurysm9", "jpkrohling", "djaglowski"]
    maintainers = ["mx-psi", "bogdandrutu", "codeboten", "dmitryax"]
}

module "docs_sig" {
    source = "./modules/sig"
    name = "docs"
    triagers = []
    approvers = ["tedsuo", "paulsbruce"]
    maintainers = ["svrnm", "mtwo", "cartermp", "jparsana", "austinlparker", "chalin", "flands"]
}

module "javascript_sig" {
    source = "./modules/sig"
    name = "javascript"
    triagers = []
    approvers = ["haddasbronfman", "MSNev", "Flarna", "JamieDanielson", "naseemkullah", "mwear", "trentm", "pkanal", "svetlanabrennan", "martinkuba", "hectorhdzg"]
    maintainers = ["pichlermarc", "dyladan", "legendecas", "blumamir"]
}

module "java_sig" {
    source = "./modules/sig"
    name = "java"
    triagers = []
    approvers = ["trask", "breedx-splk", "jsuereth", "mateuszrzeszutek"]
    maintainers = ["jack-berg", "jkwatson"]
}

module "go_sig" {
    source = "./modules/sig"
    name = "go"
    triagers = ["alolita"]
    approvers = ["hanyuancheung", "dmathieu", "XSAM", "evantorrie", "Aneurysm9", "dashpole"]
    maintainers = ["MadVikingGod", "pellared", "MrAlias"]
}

module "technical-committee_wg" {
    source = "./modules/wg"
    name = "technical-committee"
    members = ["tigrannajaryan", "reyang", "jack-berg", "arminru", "bogdandrutu", "jsuereth", "jmacd", "yurishkuro", "carlosalberto"]
}

module "specs_sig" {
    source = "./modules/sig"
    name = "specs"
    triagers = ["rbailey7210", "andrewhsu"]
    approvers = ["tigrannajaryan", "reyang", "jack-berg", "arminru", "bogdandrutu", "jsuereth", "jmacd", "yurishkuro", "carlosalberto"]
    maintainers = []
}

module "ruby_sig" {
    source = "./modules/sig"
    name = "ruby"
    triagers = []
    approvers = ["robbkidd", "ericmustin", "arielvalentin", "ahayworth", "plantfansam"]
    maintainers = ["mwear", "fbogsany", "dazuma", "robertlaurin"]
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
    approvers = ["tydhot", "addname"]
    maintainers = ["tensorchen", "laziobird", "sunface"]
}

module "php_sig" {
    source = "./modules/sig"
    name = "php"
    triagers = ["jodeev"]
    approvers = ["morrisonlevi", "Fahmy-Mohammed", "zsistla", "kishannsangani", "beniamin"]
    maintainers = ["pdelewski", "brettmc", "tidal", "bobstrecansky"]
}

module "java-instrumentation_sig" {
    source = "./modules/sig"
    name = "java-instrumentation"
    triagers = []
    approvers = ["jack-berg", "jkwatson", "breedx-splk"]
    maintainers = ["trask", "mateuszrzeszutek", "laurit"]
}

module "opentelemetry-python-contrib_sig" {
    source = "./modules/sig"
    name = "opentelemetry-python-contrib"
    triagers = []
    approvers = ["NathanielRN", "nikosokolik", "sanketmehta28", "ashu658", "oxeye-nikolay", "owais", "aabmass", "pmcollins", "jeremydvoss", "srikanthccv"]
    maintainers = ["lzchen", "shalevr", "ocelotl"]
}

module "rust_sig" {
    source = "./modules/sig"
    name = "rust"
    triagers = []
    approvers = ["lalitb", "shaun-cox", "MikeGoldsmith", "iredelmeier", "frigus02", "awiede"]
    maintainers = ["TommyCpp", "hdost", "jtescher", "cijothomas"]
}

module "swift_sig" {
    source = "./modules/sig"
    name = "swift"
    triagers = []
    approvers = ["vvydier"]
    maintainers = ["nachoBonafonte", "bryce-b"]
}

module "collector-contrib_sig" {
    source = "./modules/sig"
    name = "collector-contrib"
    triagers = ["frzifus", "crobert-1", "gbbr", "JaredTan95", "mwear", "Frapschen", "gouthamve", "bryan-aguilar"]
    approvers = ["atoulme", "MovieStoreGuy", "dmitryax", "bogdandrutu", "TylerHelmuth", "astencel-sumo", "codeboten", "mx-psi", "Aneurysm9", "evan-bradley", "songy23", "fatsheep9146", "dashpole", "jpkrohling", "djaglowski"]
    maintainers = []
}

module "collector-contrib-maintainer_wg" {
    source = "./modules/wg"
    name = "collector-contrib-maintainer"
    members = ["MovieStoreGuy", "dmitryax", "bogdandrutu", "TylerHelmuth", "mx-psi", "codeboten", "evan-bradley", "jpkrohling", "djaglowski"]
}

module "specs-trace_sig" {
    source = "./modules/sig"
    name = "specs-trace"
    triagers = []
    approvers = ["tedsuo", "iNikem", "Oberon00"]
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
    approvers = ["RassK", "cijothomas", "macrogreg"]
    maintainers = ["zacharycmontoya", "rajkumar-rangaraj", "pjanotti", "nrcventura", "pellared", "Kielek"]
}

module "governance-committee_wg" {
    source = "./modules/wg"
    name = "governance-committee"
    members = ["dyladan", "svrnm", "alolita", "trask", "tedsuo", "danielgblanco", "mtwo", "austinlparker", "jpkrohling"]
}

module "java-contrib_sig" {
    source = "./modules/sig"
    name = "java-contrib"
    triagers = ["cyrille-leclerc", "kenfinnigan", "PeterF778", "anosek-an", "dehaansa", "willarmiros", "kittylyst", "Mrod1598", "breedx-splk", "iNikem", "oertl"]
    approvers = ["laurit"]
    maintainers = ["trask", "mateuszrzeszutek", "jack-berg"]
}

module "helm_sig" {
    source = "./modules/sig"
    name = "helm"
    triagers = ["tigrannajaryan", "naseemkullah"]
    approvers = ["Allex1", "povilasv", "puckpuck"]
    maintainers = ["dmitryax", "TylerHelmuth"]
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
    members = ["jsuereth", "punya", "alolita", "Aneurysm9", "rakyll", "dashpole"]
}

module "dotnet-contrib_sig" {
    source = "./modules/sig"
    name = "dotnet-contrib"
    triagers = []
    approvers = []
    maintainers = ["utpilla", "alanwest", "cijothomas", "CodeBlanch", "Kielek"]
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
    approvers = ["TomRoSystems", "marcalff", "ThomsonTan", "jsuereth", "esigo", "pyohannes", "maxgolov", "DebajitDas", "kpratyus", "seemk", "tobiasstadler"]
    maintainers = ["lalitb"]
}

module "proto-go_sig" {
    source = "./modules/sig"
    name = "proto-go"
    triagers = []
    approvers = ["Aneurysm9", "pellared", "MadVikingGod"]
    maintainers = ["MikeGoldsmith", "MrAlias"]
}

module "erlang-contrib_sig" {
    source = "./modules/sig"
    name = "erlang-contrib"
    triagers = []
    approvers = ["hauleth", "zachdaniel", "deadtrickster", "ferd", "GregMefford"]
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
    approvers = ["jsuereth", "weyert", "alolita"]
    maintainers = ["aabmass", "sjs994", "srikanthccv"]
}

module "opamp-go_sig" {
    source = "./modules/sig"
    name = "opamp-go"
    triagers = []
    approvers = ["djaglowski", "Aneurysm9", "codeboten", "srikanthccv"]
    maintainers = ["tigrannajaryan", "andykellr"]
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
    members = ["tigrannajaryan", "kenfinnigan", "arminru", "joaopgrassi", "dpauls", "MovieStoreGuy", "denisivan0v", "trask", "tedsuo", "pyohannes", "jamesmoessis", "lmolkova"]
}

module "blog_sig" {
    source = "./modules/sig"
    name = "blog"
    triagers = []
    approvers = ["mtwo", "cartermp", "SergeyKanzhelev", "austinlparker", "svrnm", "alolita"]
    maintainers = []
}

module "ruby-contrib_sig" {
    source = "./modules/sig"
    name = "ruby-contrib"
    triagers = []
    approvers = ["simi", "kaylareopelle"]
    maintainers = ["dazuma", "robbkidd", "mwear", "arielvalentin", "ericmustin", "ahayworth", "robertlaurin", "fbogsany", "plantfansam"]
}

module "demo_sig" {
    source = "./modules/sig"
    name = "demo"
    triagers = []
    approvers = ["reyang", "wph95", "cedricziel", "fatsheep9146", "mviitane"]
    maintainers = ["austinlparker", "cartersocha", "julianocosta89", "puckpuck"]
}

module "sandbox-web-js_sig" {
    source = "./modules/sig"
    name = "sandbox-web-js"
    triagers = []
    approvers = []
    maintainers = ["tedsuo", "dyladan", "martinkuba", "MSNev"]
}

module "go-instrumentation_sig" {
    source = "./modules/sig"
    name = "go-instrumentation"
    triagers = ["jmacd"]
    approvers = ["RonFed", "damemi", "dineshg13", "MadVikingGod", "pellared"]
    maintainers = ["MikeGoldsmith", "edeNFed", "MrAlias", "pdelewski"]
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
    members = ["mhausenblas", "musingvirtual", "sharrmander", "reese-lee", "avillela"]
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
    approvers = ["Oberon00", "MovieStoreGuy", "tedsuo", "pyohannes", "jamesmoessis", "lmolkova"]
    maintainers = ["reyang", "arminru", "joaopgrassi", "jsuereth", "AlexanderWert"]
}

module "configuration_sig" {
    source = "./modules/sig"
    name = "configuration"
    triagers = []
    approvers = []
    maintainers = ["jack-berg", "tsloughter", "codeboten", "MrAlias"]
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
    approvers = ["trask", "jonatan-ivanov", "mateuszrzeszutek", "jack-berg"]
    maintainers = []
}

module "sig-security_sig" {
    source = "./modules/sig"
    name = "sig-security"
    triagers = []
    approvers = []
    maintainers = ["reyang", "jpkrohling", "codeboten", "cartersocha"]
}

module "android_sig" {
    source = "./modules/sig"
    name = "android"
    triagers = []
    approvers = ["trask", "jack-berg"]
    maintainers = ["breedx-splk", "LikeTheSalad"]
}

module "semconv-system_sig" {
    source = "./modules/sig"
    name = "semconv-system"
    triagers = []
    approvers = ["dmitryax", "mx-psi", "ChrsMark", "frzifus"]
    maintainers = []
}

module "semconv-mobile_sig" {
    source = "./modules/sig"
    name = "semconv-mobile"
    triagers = []
    approvers = ["breedx-splk", "LikeTheSalad", "surbhiia", "nachoBonafonte", "bryce-b"]
    maintainers = []
}

module "semconv-dotnet-approver_wg" {
    source = "./modules/wg"
    name = "semconv-dotnet-approver"
    members = ["noahfalk", "JamesNK", "antonfirsov"]
}

module "semconv-container_sig" {
    source = "./modules/sig"
    name = "semconv-container"
    triagers = []
    approvers = ["jinja2", "frzifus", "dmitryax", "TylerHelmuth", "mx-psi", "ChrsMark"]
    maintainers = []
}

module "semconv-k8s_sig" {
    source = "./modules/sig"
    name = "semconv-k8s"
    triagers = []
    approvers = ["jinja2", "frzifus", "dmitryax", "dashpole", "TylerHelmuth", "mx-psi", "ChrsMark"]
    maintainers = []
}

module "operator_sig" {
    source = "./modules/sig"
    name = "operator"
    triagers = []
    approvers = ["swiatekm-sumo", "frzifus", "dmitryax", "TylerHelmuth", "yuriolisa"]
    maintainers = ["jpkrohling", "VineethReddy02", "jaronoff97", "pavolloffay"]
}

module "operator-ta_sig" {
    source = "./modules/sig"
    name = "operator-ta"
    triagers = []
    approvers = []
    maintainers = ["jaronoff97", "kristinapathak", "Aneurysm9", "VineethReddy02", "secustor", "jpkrohling", "pavolloffay"]
}
