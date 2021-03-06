#
# OMNeT++/OMNEST Makefile for test2
#
# This file was generated with the command:
#  opp_makemake -f --deep -O out -I../queueinglib -L../queueinglib/out/$$\(CONFIGNAME\) -lqueueinglib -DQUEUEING_IMPORT -KQUEUEINGLIB_PROJ=../queueinglib
#

# Name of target to be created (-o option)
TARGET = test2$(EXE_SUFFIX)

# User interface (uncomment one) (-u option)
USERIF_LIBS = $(ALL_ENV_LIBS) # that is, $(TKENV_LIBS) $(CMDENV_LIBS)
#USERIF_LIBS = $(CMDENV_LIBS)
#USERIF_LIBS = $(TKENV_LIBS)

# C++ include paths (with -I)
INCLUDE_PATH = -I../queueinglib -I. -Iresults

# Additional object and library files to link with
EXTRA_OBJS =

# Additional libraries (-L, -l options)
LIBS = -L../queueinglib/out/$(CONFIGNAME)  -lqueueinglib
LIBS += -Wl,-rpath,`abspath ../queueinglib/out/$(CONFIGNAME)`

# Output directory
PROJECT_OUTPUT_DIR = out
PROJECTRELATIVE_PATH =
O = $(PROJECT_OUTPUT_DIR)/$(CONFIGNAME)/$(PROJECTRELATIVE_PATH)

# Object files for local .cc and .msg files
OBJS = $O/DataDelay.o $O/PacketSource.o $O/SinkStat.o $O/DataPacket_m.o

# Message files
MSGFILES = \
    DataPacket.msg

# Other makefile variables (-K)
QUEUEINGLIB_PROJ=../queueinglib

#------------------------------------------------------------------------------

# Pull in OMNeT++ configuration (Makefile.inc or configuser.vc)

ifneq ("$(OMNETPP_CONFIGFILE)","")
CONFIGFILE = $(OMNETPP_CONFIGFILE)
else
ifneq ("$(OMNETPP_ROOT)","")
CONFIGFILE = $(OMNETPP_ROOT)/Makefile.inc
else
CONFIGFILE = $(shell opp_configfilepath)
endif
endif

ifeq ("$(wildcard $(CONFIGFILE))","")
$(error Config file '$(CONFIGFILE)' does not exist -- add the OMNeT++ bin directory to the path so that opp_configfilepath can be found, or set the OMNETPP_CONFIGFILE variable to point to Makefile.inc)
endif

include $(CONFIGFILE)

# Simulation kernel and user interface libraries
OMNETPP_LIB_SUBDIR = $(OMNETPP_LIB_DIR)/$(TOOLCHAIN_NAME)
OMNETPP_LIBS = -L"$(OMNETPP_LIB_SUBDIR)" -L"$(OMNETPP_LIB_DIR)" -loppmain$D $(USERIF_LIBS) $(KERNEL_LIBS) $(SYS_LIBS)

COPTS = $(CFLAGS) -DQUEUEING_IMPORT $(INCLUDE_PATH) -I$(OMNETPP_INCL_DIR)
MSGCOPTS = $(INCLUDE_PATH)

# we want to recompile everything if COPTS changes,
# so we store COPTS into $COPTS_FILE and have object
# files depend on it (except when "make depend" was called)
COPTS_FILE = $O/.last-copts
ifneq ($(MAKECMDGOALS),depend)
ifneq ("$(COPTS)","$(shell cat $(COPTS_FILE) 2>/dev/null || echo '')")
$(shell $(MKPATH) "$O" && echo "$(COPTS)" >$(COPTS_FILE))
endif
endif

#------------------------------------------------------------------------------
# User-supplied makefile fragment(s)
# >>>
# <<<
#------------------------------------------------------------------------------

# Main target
all: $O/$(TARGET)
	$(Q)$(LN) $O/$(TARGET) .

$O/$(TARGET): $(OBJS)  $(wildcard $(EXTRA_OBJS)) Makefile
	@$(MKPATH) $O
	@echo Creating executable: $@
	$(Q)$(CXX) $(LDFLAGS) -o $O/$(TARGET)  $(OBJS) $(EXTRA_OBJS) $(AS_NEEDED_OFF) $(WHOLE_ARCHIVE_ON) $(LIBS) $(WHOLE_ARCHIVE_OFF) $(OMNETPP_LIBS)

.PHONY: all clean cleanall depend msgheaders

.SUFFIXES: .cc

$O/%.o: %.cc $(COPTS_FILE)
	@$(MKPATH) $(dir $@)
	$(qecho) "$<"
	$(Q)$(CXX) -c $(CXXFLAGS) $(COPTS) -o $@ $<

%_m.cc %_m.h: %.msg
	$(qecho) MSGC: $<
	$(Q)$(MSGC) -s _m.cc $(MSGCOPTS) $?

msgheaders: $(MSGFILES:.msg=_m.h)

clean:
	$(qecho) Cleaning...
	$(Q)-rm -rf $O
	$(Q)-rm -f test2 test2.exe libtest2.so libtest2.a libtest2.dll libtest2.dylib
	$(Q)-rm -f ./*_m.cc ./*_m.h
	$(Q)-rm -f results/*_m.cc results/*_m.h

cleanall: clean
	$(Q)-rm -rf $(PROJECT_OUTPUT_DIR)

depend:
	$(qecho) Creating dependencies...
	$(Q)$(MAKEDEPEND) $(INCLUDE_PATH) -f Makefile -P\$$O/ -- $(MSG_CC_FILES)  ./*.cc results/*.cc

# DO NOT DELETE THIS LINE -- make depend depends on it.
$O/DataDelay.o: DataDelay.cc \
	$(QUEUEINGLIB_PROJ)/Delay.h \
	$(QUEUEINGLIB_PROJ)/QueueingDefs.h \
	DataDelay.h
$O/DataPacket_m.o: DataPacket_m.cc \
	$(QUEUEINGLIB_PROJ)/Job.h \
	$(QUEUEINGLIB_PROJ)/Job_m.h \
	$(QUEUEINGLIB_PROJ)/QueueingDefs.h \
	DataPacket_m.h
$O/PacketSource.o: PacketSource.cc \
	$(QUEUEINGLIB_PROJ)/Job.h \
	$(QUEUEINGLIB_PROJ)/Job_m.h \
	$(QUEUEINGLIB_PROJ)/QueueingDefs.h \
	$(QUEUEINGLIB_PROJ)/Source.h \
	DataPacket_m.h \
	PacketSource.h
$O/SinkStat.o: SinkStat.cc \
	$(QUEUEINGLIB_PROJ)/Job.h \
	$(QUEUEINGLIB_PROJ)/Job_m.h \
	$(QUEUEINGLIB_PROJ)/QueueingDefs.h \
	$(QUEUEINGLIB_PROJ)/Sink.h \
	DataPacket_m.h \
	SinkStat.h

