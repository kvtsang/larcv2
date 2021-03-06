#!/usr/bin/env python
import ROOT, sys
from ROOT import std
from larcv import larcv

if len(sys.argv) < 2:

   print 'Usage: python',sys.argv[0],'CONFIG_FILE [LARCV_FILE1 LARCV_FILE2 ...]'
   sys.exit(1)

proc = larcv.ProcessDriver('ProcessDriver')

proc.configure(sys.argv[1])

if len(sys.argv) > 1:
   
   flist=ROOT.std.vector('std::string')()
   for x in xrange(len(sys.argv)-3):
      flist.push_back(sys.argv[x+3])

   proc.override_input_file(flist)


reco_id = proc.process_id("LArbysImage")
ana_id  = proc.process_id("LArbysImageAna")

larbysimg     = proc.process_ptr(reco_id)
larbysimg_ana = proc.process_ptr(ana_id)
larbysimg_ana.SetManager(larbysimg.Manager())

#evstart=int(sys.argv[2])
#step=int(3434)
#step=int(1654)

#print "got start: ",evstart," step: ",step
#proc.override_ana_file("numu_ccqe_p00_p07_rad6_p60_%05d_%05d.root"%(evstart,evstart+step))

proc.initialize()
#proc.batch_process(evstart,step)
#proc.batch_process(0,10)
proc.batch_process()

proc.finalize()
