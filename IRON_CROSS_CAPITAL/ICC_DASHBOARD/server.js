import { handler } from './build/handler.js';
import express from 'express';
import { createServer } from 'http';
import { Server } from 'socket.io';

const app = express();
const server = createServer(app);
const io = new Server(server, {
    cors: { origin: "*" }
});

io.on('connection', (socket) => {
    console.log('🛡️ Engine Connected');
    socket.on('new_whale', (data) => {
        io.emit('new_whale', data);
    });
});

app.use(handler);

const port = process.env.PORT || 3000;
server.listen(port, () => {
    print(`✅ Dashboard Server running on port ${port}`);
});