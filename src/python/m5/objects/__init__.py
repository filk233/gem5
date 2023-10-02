# Copyright (c) 2010 The Hewlett-Packard Development Company
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

for module in __spec__.loader_state:
    if module.startswith("m5.objects."):
        exec(f"from {module} import *")

from Tlm import *
from SystemC import *
from TlmBridge import *
from X86SeWorkload import *
from X86FsWorkload import *
from X86Decoder import *
from X86ISA import *
from X86LocalApic import *
from X86MMU import *
from X86NativeTrace import *
from X86TLB import *
from X86CPU import *
from E820 import *
from SMBios import *
from IntelMP import *
from ACPI import *
from X86KvmCPU import *
from BaseInterrupts import *
from BaseISA import *
from BaseMMU import *
from BaseTLB import *
from InstDecoder import *
from ClockedObject import *
from TickedObject import *
from Workload import *
from Root import *
from ClockDomain import *
from VoltageDomain import *
from System import *
from DVFSHandler import *
from SubSystem import *
from RedirectPath import *
from PowerState import *
from PowerDomain import *
from SignalPort import *
from InstTracer import *
from Process import *
from MathExprPowerModel import *
from PowerModel import *
from PowerModelState import *
from ThermalDomain import *
from ThermalModel import *
from Probe import *
from FuncUnit import *
from StaticInstFlags import *
from InstPBTrace import *
from CheckerCPU import *
from BaseCPU import *
from CpuCluster import *
from CPUTracers import *
from TimingExpr import *
from DummyChecker import *
from BaseMinorCPU import *
from MinorCPU import *
from PcCountTracker import *
from GarnetSyntheticTraffic import *
from BaseTrafficGen import *
from GUPSGen import *
from PyTrafficGen import *
from TrafficGen import *
from MemTest import *
from RubyTester import *
from RubyDirectedTester import *
from KvmVM import *
from BaseKvmCPU import *
from BranchPredictor import *
from FUPool import *
from FuncUnitConfig import *
from BaseO3CPU import *
from BaseO3Checker import *
from O3CPU import *
from O3Checker import *
from SimpleTrace import *
from ElasticTrace import *
from BaseAtomicSimpleCPU import *
from BaseNonCachingSimpleCPU import *
from BaseTimingSimpleCPU import *
from BaseSimpleCPU import *
from AtomicSimpleCPU import *
from NonCachingSimpleCPU import *
from TimingSimpleCPU import *
from SimPoint import *
from TraceCPU import *
from CommMonitor import *
from AbstractMemory import *
from AddrMapper import *
from Bridge import *
from SysBridge import *
from MemCtrl import *
from HeteroMemCtrl import *
from HBMCtrl import *
from MemInterface import *
from DRAMInterface import *
from NVMInterface import *
from ExternalMaster import *
from ExternalSlave import *
from CfiMemory import *
from SharedMemoryServer import *
from SimpleMemory import *
from XBar import *
from HMCController import *
from SerialLink import *
from MemDelay import *
from PortTerminator import *
from ThreadBridge import *
from MemChecker import *
from Controller import *
from DMA_Controller import *
from Directory_Controller import *
from L1Cache_Controller import *
from L2Cache_Controller import *
from RubySystem import *
from Sequencer import *
from RubyCache import *
from DirectoryMemory import *
from RubyPrefetcher import *
from WireBuffer import *
from BasicLink import *
from BasicRouter import *
from MessageBuffer import *
from Network import *
from FaultModel import *
from SimpleLink import *
from SimpleNetwork import *
from GarnetLink import *
from GarnetNetwork import *
from BaseMemProbe import *
from StackDistProbe import *
from MemFootprintProbe import *
from MemTraceProbe import *
from Cache import *
from Tags import *
from IndexingPolicies import *
from Prefetcher import *
from Compressors import *
from ReplacementPolicies import *
from QoSMemCtrl import *
from QoSMemSinkCtrl import *
from QoSMemSinkInterface import *
from QoSPolicy import *
from QoSTurnaround import *
from OutgoingRequestBridge import *
from SimpleObject import *
from HelloObject import *
from SimpleMemobj import *
from SimpleCache import *
from Graphics import *
from Vnc import *
from BloomFilters import *
from Device import *
from IntPin import *
from ResetPort import *
from Platform import *
from BadDevice import *
from Ethernet import *
from VirtIO import *
from VirtIOConsole import *
from VirtIOBlock import *
from VirtIORng import *
from VirtIO9P import *
from Ide import *
from DiskImage import *
from SimpleDisk import *
from PciDevice import *
from PciHost import *
from CopyEngine import *
from Pc import *
from SouthBridge import *
from Cmos import *
from I8259 import *
from I8254 import *
from I8237 import *
from I8042 import *
from X86Ide import *
from PcSpeaker import *
from I82094AA import *
from X86QemuFwCfg import *
from Serial import *
from Terminal import *
from Uart import *
from I2C import *
from QemuFwCfg import *
from PS2 import *
from objects import *
from SimObject import *

