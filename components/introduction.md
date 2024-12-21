Wireless ad-hoc mesh networks (MANETs) are a significant area of development in IoT devices.
They are being deployed in a wide range of applications, from healthcare to automotive to industrial,
where permanent infrastructure can be difficult to deploy.

Mesh networks consist of a number of nodes. In the case of wireless meshes, these can be portable wireless devices,
such as IoT sensors or smartphones, and fixed devices, such as wireless access points and base stations.

In a traditional wireless network, all devices connect to a base station and perform conversations with only that one device.
This increases the cost of the base station: for example, a 4G LTE base station commonly costs [[TODO]] to deploy.

Wireless mesh networks promise to decrease the deployment cost. In a wireless mesh network, most or all devices are routing-capable.
Devices can connect to each other opportunistically and route data between each other:
this marginally increases complexity for a single device (as it now needs to maintain multiple links to its peers, and perform routing)
but massively decreases the cost of deploying base stations
(which are now needed only for linking a small number of devices back to the wider network.)

A significant source of complexity in wireless mesh networks is the routing of data
based on a changing topology.
Wireless devices can be mobile, moving in and out of range of other devices;
also, because they are mobile, they have limited battery life and thus limit their transmitted wireless power.
A wireless mesh network therefore needs to be able to respond to changes in the network topology
to ensure data packets can still get to where they need to go: this is done using a routing algorithm.

Wireless mesh networks have been successfully used in a number of applications,
from IoT to disaster response, from healthcare to military operations.
Each of these applications has its own particularities:
for example, in disaster response, the network topology is likely to be changing frequently,
but the nodes (like smartphones and specialized communicator devices) are more capable and attended by humans;
while in healthcare applications, like IoT sensors in hospitals, the network topology is likely to be more stable,
but the devices themselves are more constrained, and humans cannot alter their configuration in real time.

To our knowledge, as of 2024, there do not appear to be any scoping reviews
on the topic of routing algorithms for IoT wireless mesh networks.
With this review, we hope to fill this gap by providing a summary of the current research in the area.
We focus on resource-constrained devices and applications, in particular industrial and IoT devices.
By summarizing the research in this area, we hope to extract insights that
can inform the design of IoT wireless mesh network devices.

Our hypothesis is that in order to achieve a good balance of quality of service and energy efficiency,
routing algorithms must be specialized for the IoT wireless mesh application,
rather than using generic internet protocols.
In order to discover whether this is the case, we perform a scoping review on the topic of routing algorithms in wireless mesh networks.