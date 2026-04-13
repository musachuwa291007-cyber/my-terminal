<script lang="ts">
  import { onMount } from 'svelte';
  import { io } from 'socket.io-client';

  let orders = $state([] as any[]); 
  let status = $state("OFFLINE");

  onMount(() => {
    // This now looks at the same URL the website is hosted on
    const socket = io(); 
    
    socket.on('connect', () => { status = "ONLINE"; });
    socket.on('new_whale', (data) => {
      if (data) {
        orders = [data, ...orders].slice(0, 15);
      }
    });
    return () => socket.disconnect();
  });
</script>

<main style="background: black; color: #dc2626; min-height: 100vh; padding: 40px; font-family: monospace;">
  <div style="border-bottom: 2px solid #7f1d1d; display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px;">
    <h1 style="font-weight: 900; margin: 0; letter-spacing: 2px;">IRON CROSS CAPITAL</h1>
    <span style="font-weight: bold; color: {status === 'ONLINE' ? '#22c55e' : '#dc2626'}">● {status}</span>
  </div>
  
  <div style="margin-top: 30px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 2fr 1fr; border-bottom: 2px solid #450a0a; padding-bottom: 10px; font-size: 11px; opacity: 0.6; color: #D4AF37;">
      <span>TIMESTAMP</span><span>ASSET</span><span>PRICE</span><span>VOL (CONTRACTS)</span><span style="text-align: right;">SIDE</span>
    </div>

    {#each orders as o}
      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 2fr 1fr; border-bottom: 1px solid #1a1a1a; padding: 15px 0; align-items: center;">
        <span style="color: #52525b;">{o.time}</span>
        <span style="font-weight: bold; color: #dc2626;">{o.asset}</span>
        <span style="color: white;">{o.price}</span>
        <span style="font-size: 1.2rem; font-weight: 800; color: white;">{o.vol} <small style="opacity: 0.3;">LOTS</small></span>
        <span style="text-align: right; font-weight: bold; color: {o.side === 'SELL' ? '#ef4444' : '#22c55e'}">{o.side}</span>
      </div>
    {/each}
  </div>
</main>