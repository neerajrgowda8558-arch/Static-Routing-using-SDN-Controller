from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def install_flow(event, in_port, out_port):
    msg = of.ofp_flow_mod()
    msg.match.in_port = in_port
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

def _handle_ConnectionUp(event):

    dpid = event.dpid

    # Switch 1
    if dpid == 1:
        install_flow(event,1,2)
        install_flow(event,2,1)

    # Switch 2
    elif dpid == 2:
        install_flow(event,1,2)
        install_flow(event,2,1)

    # Switch 3
    elif dpid == 3:
        install_flow(event,1,2)
        install_flow(event,2,1)

    log.info("Static routing paths installed")

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)