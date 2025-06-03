---
layout: post
title: "EmonCMS and multiple OpenTRV nodes"
date: 2016-04-13 19:55:49 +0000
author: "Jeremy Poulter"
categories: ["Smart Home", "Energy Monitoring"]
tags: ["opentrv", "emoncms", "iot", "node-red"]
original_url: "/blog/2016/4/13/emoncms-and-multiple-opentrv-nodes"
---

As a follow up on my initial experiments with getting data from [OpenTRV to Open Energy Monitor](http://bigjungle.net/blog/2016/3/9/experiments-with-node-red), this post is going to build on that and add support for parsing data received from the other OpenTRV nodes other than the one directly connected via the USB serial.

## The Hardware

The hardware I am using is a Rev 2 board as the receiver as described [previously](http://bigjungle.net/blog/2016/3/9/experiments-with-node-red) and the transmitters are two Rev 11 boards. Due to the design of the firmware however this should work the same on any of the devices.

## Firmware

To get these to talk to each other we need to ensure the firmware for on the receiver device has the `ENABLE_STATS_RX` build option defined and on the transmitting end `ENABLE_STATS_TX` needs to be defined.

### Testing

With the new firmware built and flashed it is time to power up and see what we get. Load up the Node-RED UI with the work sheet we created last time. Turn off all the debug nodes apart from the last one of the switch node. This will now only show the console output we are not parsing, (you may need to wait about 10 mins to see anything).

You should see some JSON output that looks suspiciously like the end of the status lines from last time. It is probably of no surprise that in fact in is the same format as the JSON part of the status text. So we already have the code to parse this text.

## Parsing The Output

First things first though, we need to separate out the JSON lines from the rest of the unhandled Lines. Double click on the switch node and add a new entry above the otherwise entry. Set this to look for a regex and enter the following:

```
^{
```

This will now pull out the JSON by detecting the opening `{`.

Now connect a new function node to a new switch output and grab the JSON code we wrote before:

```javascript
var obj = JSON.parse('{'+parts[16]+'}');
for(var i in obj) 
{
    switch(i)
    {
        case '@':
            break;
        case 'T|C16':
            break;
        default:
    }
}
```

We have to make a few changes to make this stand alone. First the JSON is coming from `msg.payload` rather than parts[16] and we are going to write the parsed output back directly to `msg.payload`. The reason for this will become clear soon.

```javascript
var json = msg.payload;
msg.payload = {};

var obj = JSON.parse(json);
for(var i in obj) 
{
    switch(i)
    {
        case '@':
            break;
        case 'T|C16':
            break;
        default:
    }
}

return msg;
```

## Sending to EmonCMS

Now all that is left to do disconnect the function output to the EmonCMS node, or is it? You may have noticed I the previous example that we entered the EmonCMS node ID in the settings of the EmonCMS node in Node-RED. Now we are receiving from more than one OpenTRV device we need to translate the OpenTRV ID to an EmonCMS node ID. So we need to write a function to map the IDs from one system to another.

Place a function node after the two parsing nodes and before the EmonCMS node:

Our parsing code is writing the OpenTRV ID in to `msg.nodeid` and if the `Node` setting is left blank the EmonCMS node will use `msg.nodegroup` for the `Node`. This can be done with the following:

```javascript
var nodeMapping = {
    'f9ea': 26,
    'a7de': 27
};

if(msg.nodeid && nodeMapping[msg.nodeid]) {
    msg.nodegroup = nodeMapping[msg.nodeid];
}

return msg;
```

You will need to alter the content of `nodeMapping` for your environment.

As we are dealing with more than just `msg.payload` it is handy to debug the whole `msg object`. To do this you can open a debug node's settings (double click it) and change the Output to `complete msg object`.

The other change we need to make is to clear the fixed `Node` setting in the EmonCMS node. Open the EmonCMS node settings and delete anything in the `Node` setting. Don't worry if the setting highlights red, this can be ignored as we are passing in the setting for this value. A warning may also be given when deploying, this too can be ignored.

We can now deploy the sheet and it should look something like this.

If all is working you should now see all the OpenTRV nodes showing data in your EmonCMS.

## Making Improvements

We could leave it there, but there is a bit of tidy up we can do to help reduce the maintenance. For example the newer versions of the firmware send the battery level using `B|cV`. To add support for this we would have to edit two similar pieces of code. We can easily update the code to put all the JSON parsing in a single node.

Instead of parsing the JSON in the `OpenTRV Parse Status` we can pass the JSON along to the `OpenTRV Parse JSON` node so it can be parse there. Let's disconnect the output of the `OpenTRV Parse Status` from the EmonCMS node and to the input of the `OpenTRV Parse JSON` so we have a unified parsing approach.

This approach provides a more maintainable solution for handling multiple OpenTRV nodes and ensures consistent data processing across all connected devices.
