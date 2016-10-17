#!/usr/bin/env python2
# Copyright (c) 2014-2015 The Bitcoin Core developers
# Copyright (c) 2015-2016 The Bitcoin Unlimited developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.


from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import *

class ParallelTest (BitcoinTestFramework):

    def setup_chain(self):
        print("Initializing test directory "+self.options.tmpdir)
        initialize_chain_clean(self.options.tmpdir, 4)

    def setup_network(self, split=False):
        self.nodes = []
        self.nodes.append(start_node(0, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(1, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(2, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(3, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        connect_nodes_bi(self.nodes,0,1)
        connect_nodes_bi(self.nodes,1,2)
        connect_nodes_bi(self.nodes,0,2)
        connect_nodes_bi(self.nodes,1,3)
        self.is_network_split=False
        self.sync_all()

    def run_test (self):
        print "Mining blocks..."

        # Mine some blocks on node2 which we will need at the end to generate a few transactions from that node
        # in order to create the small block with just a few transactions in it.
        self.nodes[2].generate(1)
        self.sync_all()

        # Mine the rest on node0 where we will generate the bigger block.
        self.nodes[0].generate(100)
        self.sync_all()
 
        self.nodes[0].generate(100)
        self.sync_all()

        # Stop and restart nodes
        stop_nodes(self.nodes)
        wait_bitcoinds()

        self.nodes = []
        self.nodes.append(start_node(0, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(1, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(2, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(3, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))

        # Create many utxo's
        print "Generating txns..."
        send_to = {}
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)
        self.nodes[0].keypoolrefill(100)
        self.nodes[0].keypoolrefill(100)
        for i in xrange(200):
            send_to[self.nodes[0].getnewaddress()] = Decimal("0.01")
        self.nodes[0].sendmany("", send_to)

        # Mine a block so that the utxos are now spendable
        self.nodes[0].generate(1)

        connect_nodes_bi(self.nodes,0,1)
        connect_nodes_bi(self.nodes,1,2)
        connect_nodes_bi(self.nodes,0,2)
        connect_nodes_bi(self.nodes,1,3)
        self.is_network_split=False
        self.sync_all()

        # Stop and restart nodes
        stop_nodes(self.nodes)
        wait_bitcoinds()

        self.nodes = []
        self.nodes.append(start_node(0, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(1, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(2, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(3, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))

        # Send more transactions
        print "Generating more txns..."
        output_total = Decimal(0)
        j = 0
        self.utxo = self.nodes[0].listunspent()
        utxo = self.utxo.pop()
        txns_to_send = []
        num_txns = 700
        #vout = False
        while j <= num_txns:
            inputs = []
            outputs = {}
            utxo = self.utxo.pop()
            if utxo["amount"] > Decimal("0.0100000") or utxo["amount"] < Decimal("0.0100000"):
                continue
            if utxo["spendable"] is True:
                j = j + 1
                inputs.append({ "txid" : utxo["txid"], "vout" : utxo["vout"]})
                #inputs.append({ "txid" : utxo["txid"], "vout" : vout['n'], "scriptPubKey" : vout["scriptPubKey"]["hex"]})
                outputs[self.nodes[0].getnewaddress()] = utxo["amount"] - Decimal("0.000010000")
                raw_tx = self.nodes[0].createrawtransaction(inputs, outputs)
                txns_to_send.append(self.nodes[0].signrawtransaction(raw_tx))

                # send the transaction
        for i in xrange(num_txns):
            self.nodes[0].sendrawtransaction(txns_to_send[i]["hex"], True)
        while self.nodes[0].getmempoolinfo()['size'] < num_txns:
            time.sleep(1)

        self.nodes[0].generate(1)
        connect_nodes(self.nodes[0],1)
        connect_nodes(self.nodes[1],2)
        connect_nodes(self.nodes[1],3)
        self.sync_all()


        #stop and restart nodes
        stop_nodes(self.nodes)
        wait_bitcoinds()

        self.nodes = []
        self.nodes.append(start_node(0, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(1, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(2, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))
        self.nodes.append(start_node(3, self.options.tmpdir, ["-debug", "-use-thinblocks=0", "-excessiveblocksize=6000000", "-blockprioritysize=6000000", "-blockmaxsize=6000000"]))


        # create transactions with many inputs
        print "Generating even more txns..."
        num_txns2 = 5
        self.utxo = self.nodes[0].listunspent()
        for i in xrange(num_txns2):
            inputs = []
            outputs = {}
            output_total = Decimal(0)
            j = 1
            print "utxo length " + str(len(self.utxo))
            txns_to_send = []
            while j < 600:
                utxo = self.utxo.pop()
                if utxo["amount"] > Decimal("0.0100000") or utxo["amount"] < Decimal("0.0100000"):
                    continue
                j = j + 1
                inputs.append({ "txid" : utxo["txid"], "vout" : utxo["vout"]})
                output_total = output_total + utxo["amount"]
            outputs[self.nodes[0].getnewaddress()] = output_total/2 - Decimal("0.001")
            outputs[self.nodes[0].getnewaddress()] = output_total/2 - Decimal("0.001")
            raw_tx = self.nodes[0].createrawtransaction(inputs, outputs)
            txns_to_send.append(self.nodes[0].signrawtransaction(raw_tx))
    
            # send the transactions
            self.nodes[0].sendrawtransaction(txns_to_send[0]["hex"], True)

        # Send big tx's which will now have many inputs
        num_range = 50
        for i in xrange(num_range):
            self.nodes[0].sendtoaddress(self.nodes[0].getnewaddress(), 1)

        while self.nodes[0].getmempoolinfo()['size'] < (num_txns2 + num_range):
            time.sleep(1)

        # Send a few transactions from node2 that will get mined so that we will have at least
        # a few inputs to check when the two competing blocks enter parallel validation.
        for i in xrange(10):
            self.nodes[2].sendtoaddress(self.nodes[2].getnewaddress(), "0.01")

        # Have node0 and node2 mine the same block which will compete to advance the chaintip when
        # The nodes are connected back together.
        self.nodes[0].generate(1)
        self.nodes[2].generate(1)
        connect_nodes(self.nodes[0],1)
        connect_nodes(self.nodes[1],2)
        sync_blocks(self.nodes[0:2])


        # node0 has the bigger block and was sent and began processing first, however the block from node2
        # should have come in after and beaten node0's block.  Therefore the blockhash from chaintip from 
        # node2 should now match the blockhash from the chaintip on node1; and node0 and node1 should not match.
        time.sleep(15) # wait here to make sure a re-org does not happen on node0 so we want to give it some time.
        assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())
        assert_not_equal(self.nodes[0].getbestblockhash(), self.nodes[1].getbestblockhash())


        # mine a block on node3 and then connect to the others.  This tests when a third block arrives after
        # the tip has been advanced.
        # this block should propagate to the other nodes but not cause a re-org
        self.nodes[3].generate(1)
        connect_nodes(self.nodes[1],3)
        sync_blocks(self.nodes)

        time.sleep(15) # wait here to make sure a re-org does not happen on node0 so we want to give it some time.
        assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())
        assert_not_equal(self.nodes[0].getbestblockhash(), self.nodes[1].getbestblockhash())
        assert_not_equal(self.nodes[1].getbestblockhash(), self.nodes[3].getbestblockhash())


        # Send some transactions and Mine a block on node 2.  
        # This should cause node0 to re-org and all chains should now match.
        for i in xrange(5):
            self.nodes[2].sendtoaddress(self.nodes[2].getnewaddress(), .01)
        self.nodes[2].generate(1)
        sync_blocks(self.nodes)
        assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())
        assert_equal(self.nodes[0].getbestblockhash(), self.nodes[1].getbestblockhash())

        #stop nodes
        stop_nodes(self.nodes)
        wait_bitcoinds()

if __name__ == '__main__':
    ParallelTest ().main ()
