import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // This allows Tailwind and TypeScript to work correctly on the server
    preprocess: vitePreprocess(),

    compilerOptions: {
        // Force runes mode for the project
        runes: ({ filename }) => (filename.split(/[/\\]/).includes('node_modules') ? undefined : true)
    },

    kit: {
        // We are using adapter-node so the server stays alive for your Python data
        adapter: adapter(),
        
        // This helps prevent connection issues on some hosts
        csrf: {
            checkOrigin: false,
        }
    }
};

export default config;