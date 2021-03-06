def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  conf.check_cxx(lib="clucene-core", mandatory=True, errmsg="Please install CLucene from http://clucene.sourceforge.net")

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]
  obj.target = "clucene"
  obj.source = "src/clucene_bindings.cpp"
  obj.lib = "clucene-core"