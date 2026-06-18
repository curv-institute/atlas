# Fleet operating guide (optional multi-machine layer)

`fleet.yaml` (copy from `fleet.example.yaml`) is the source of truth for the machines this program
runs on. Consult it before doing anything on a specific node.

## Network choice
Use the right network for the job: management/SSH over the LAN; high-volume storage and node-to-node
traffic over the fast fabric. Don't push large data over the slow path when a fast address exists.

## Discovery & troubleshooting discipline
When a node is unreachable or its address is unknown, work the **authoritative sources first** — do
not jump to raw network probing (it's slow, and credential/host guessing trips safety guardrails and
looks like an attack).

1. **Start from the inventory** — `fleet.yaml` has each node's recorded IP, MAC, and reachability notes.
2. **For a moved/unknown IP, use authoritative sources, not scanning** — the node's own console
   (`ip -4 -br addr`), the router/DHCP lease table, or the known MAC matched against `ip neigh`. A MAC
   OUI lookup identifies *what* a mystery host is (vendor) without logging in.
3. **If a host is L2-unreachable (ARP INCOMPLETE / no reply): report it and STOP.** Don't escalate to
   subnet sweeps, port scans, or trying credentials on guessed hosts.
4. **Scan / credential-test ONLY on explicit authorization**, and even then never spray credentials
   across guessed hosts — one named host, one stated credential, then stop.
5. **A wedged-but-pingable node** (ICMP + TCP:22 OK but SSH session hangs) is usually host-side, not
   the network; confirm with a second path + a known-good control node before touching the network.

## Change hygiene
- Prefer non-destructive checks first (`hostname`, `ip addr`, `df -h`, `findmnt`).
- Don't reboot, repartition, or change network/cluster config unless explicitly asked.
- Record durable changes back into `fleet.yaml`.
- Out-of-bounds work (another thread's node/experiment) is gated by `/mediate`, not by halting.
