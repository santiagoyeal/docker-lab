<template>
  <div style="font-family: system-ui, sans-serif; padding: 2rem;">
    <h1>Docker Lab - Vue Frontend</h1>
    <p>This is a tiny Vue 3 app served by Vite (dev mode with hot-reload).</p>
    <p>
      API status: <strong>{{ status }}</strong>
    </p>
    <button @click="checkApi">Check backend /db</button>
  </div>
</template>

<script>
export default {
  data() {
    return { status: 'unknown' }
  },
  methods: {
    async checkApi() {
      try {
        const res = await fetch('/api/ping');
        if (!res.ok) throw new Error('no ok')
        const data = await res.text();
        this.status = `OK (${data})`;
      } catch (err) {
        this.status = 'unreachable'
      }
    }
  }
}
</script>
