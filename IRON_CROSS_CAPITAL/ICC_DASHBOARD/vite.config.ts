import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { Server } from 'socket.io';

export default defineConfig({
	plugins: [
		sveltekit(),
		{
			name: 'sveltekit-socket-io',
			configureServer(server) {
				if (!server.httpServer) return;
				const io = new Server(server.httpServer);

				io.on('connection', (socket) => {
					console.log('🛡️ ICC Bridge: Python Engine Linked');

					socket.on('new_whale', (data) => {
						io.emit('new_whale', data);
					});
				});
			}
		}
	]
});