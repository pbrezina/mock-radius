#!/usr/bin/python3
# Based on https://github.com/pyradius/pyrad/blob/master/example/server.py

from pyrad import dictionary, packet, server


class MockServer(server.Server):
    def HandleAuthPacket(self, pkt):
        print("Received an authentication request")
        print("Attributes: ")
        for attr in pkt.keys():
            print("%s: %s" % (attr, pkt[attr]))

        if "State" not in pkt.keys():
            reply = self.challenge(pkt)
        else:
            reply = self.accept(pkt)

        self.SendReplyPacket(pkt.fd, reply)

    def HandleDisconnectPacket(self, pkt):
        print("Received an disconnect request")
        print("Attributes: ")
        for attr in pkt.keys():
            print("%s: %s" % (attr, pkt[attr]))

        reply = self.CreateReplyPacket(pkt)
        # COA NAK
        reply.code = 45
        self.SendReplyPacket(pkt.fd, reply)

    def accept(self, pkt):
        reply = self.CreateReplyPacket(pkt, **{
            "Service-Type": "Framed-User",
            "Framed-IP-Address": '192.168.0.1',
            "Framed-IPv6-Prefix": "fc66::1/64"
        })

        reply.code = packet.AccessAccept
        return reply

    def challenge(self, pkt):
        reply = self.CreateReplyPacket(pkt, **{
            "State": b"My State",
            "Reply-Message": "Enter more information"
        })

        reply.code = packet.AccessChallenge
        return reply


if __name__ == '__main__':
    srv = MockServer(dict=dictionary.Dictionary("dictionary"))
    srv.hosts["127.0.0.1"] = server.RemoteHost("127.0.0.1", b"Secret123", "localhost")
    srv.BindToAddress("0.0.0.0")
    srv.Run()
