# import Python IVI
import ivi
# connect to scope
scope = ivi.agilent.agilentDSOX3014A("TCPIP0::10.101.54.151::INSTR")
#scope = ivi.agilent.agilentMSO7104A("TCPIP0::192.168.1.104::INSTR")
#scope = ivi.tektronix.tektronixMDO4104("TCPIP0::192.168.1.108::INSTR")
#scope = ivi.agilent.agilentMSO7104A("USB0::2391::5973::MY********::INSTR")
#scope = ivi.tektronix.tektronixMDO4104("USB0::1689::1036::C******::INSTR")
# configure timebase
scope.acquisition.time_per_record = 1e-3
# configure triggering
scope.trigger.type = 'edge'
scope.trigger.source = scope.channels[0]
scope.trigger.coupling = 'dc'
scope.trigger.edge.slope = 'positive'
scope.trigger.level = 0
# configure channels
for ch in scope.channels[0:1]:
    ch.enabled = True
    ch.offset = 0
    ch.range = 4
    ch.coupling = 'dc'
# initiate measurement
scope.measurement.initiate()
# read out channel 1 waveform data
waveform = scope.channels[0].measurement.fetch_waveform()
# measure peak-to-peak voltage
vpp = scope.channels[0].measurement.fetch_waveform_measurement("voltage_peak_to_peak")
# measure phase
phase = scope.channels[0].measurement.fetch_waveform_measurement("phase", scope.channels[1])
# save screenshot to file
png = scope.display.fetch_screenshot()
with open('screenshot.png', 'wb') as f:
    f.write(png)
# save setup to file
setup = scope.system.fetch_setup()
with open('setup.dat', 'wb') as f:
    f.write(setup)
# restore setup from file
with open('setup.dat', 'rb') as f:
    setup = f.read()
scope.system.load_setup(setup)
