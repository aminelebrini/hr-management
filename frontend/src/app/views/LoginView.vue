<template>
  <div class="min-h-screen flex">
    <div class="hidden lg:flex w-1/2 bg-[#0a0a0a] items-center justify-center relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80"
        alt="Team collaboration"
        class="absolute inset-0 w-full h-full object-cover opacity-60"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent"></div>
      <div class="relative z-10 text-center px-12">
        <svg class="w-16 h-16 mx-auto mb-6" viewBox="0 0 56 56" fill="none">
          <rect width="56" height="56" rx="12" fill="white"/>
          <path d="M18 38V18h6l8 14V18h6v20h-6l-8-14v14h-6z" fill="#0a0a0a"/>
        </svg>
        <h2 class="text-3xl font-bold text-white mb-3">HR Management</h2>
        <p class="text-zinc-400 text-sm max-w-sm mx-auto leading-relaxed">
          Streamline your workforce management with our comprehensive HR solution.
        </p>
      </div>
    </div>

    <div class="w-full lg:w-1/2 flex items-center justify-center bg-[#0a0a0a] px-6">
      <div class="w-full max-w-sm">
        <div class="lg:hidden text-center mb-10">
          <svg class="w-12 h-12 mx-auto mb-4" viewBox="0 0 56 56" fill="none">
            <rect width="56" height="56" rx="12" fill="white"/>
            <path d="M18 38V18h6l8 14V18h6v20h-6l-8-14v14h-6z" fill="#0a0a0a"/>
          </svg>
          <h1 class="text-xl font-bold text-white">HR Management</h1>
        </div>

        <div class="mb-10">
          <h3 class="text-xl font-bold text-white">Welcome back</h3>
          <p class="text-zinc-500 text-sm mt-1">Sign in to your account to continue</p>
        </div>

        <form @submit.prevent="handleLogin">
          <div class="mb-6">
            <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Email</label>
            <input
              v-model="email"
              type="email"
              placeholder="Enter your email"
              class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
            />
          </div>

          <div class="mb-6">
            <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Password</label>
            <input
              v-model="password"
              type="password"
              placeholder="Enter your password"
              class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
            />
          </div>

          <div class="flex items-center justify-between mb-8">
            <label class="flex items-center gap-2 text-sm text-zinc-500 cursor-pointer select-none group">
              <input type="checkbox" v-model="remember" class="peer sr-only" />
              <span class="w-4 h-4 border border-zinc-700 rounded flex items-center justify-center peer-checked:bg-white peer-checked:border-white transition-colors group-hover:border-zinc-500">
                <svg v-if="remember" class="w-3 h-3 text-black" fill="currentColor" viewBox="0 0 12 12">
                  <path d="M3.5 6.5l2 2 3-4" stroke="currentColor" stroke-width="1.5" fill="none"/>
                </svg>
              </span>
              Remember me
            </label>
            <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">Forgot password?</a>
          </div>

          <button
            type="submit"
            class="w-full py-3 bg-white text-black text-sm font-semibold rounded hover:bg-zinc-200 transition-colors"
          >
            Sign In
          </button>
        </form>

        <p class="text-center text-zinc-700 text-xs mt-10">
          &copy; 2026 HR Management System
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import api from '../service/api';
export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      remember: false
    }
  },
  methods: {
    async handleLogin() {
      try {
        const response = await api.post('/login', {
          email: this.email,
          password: this.password,
          remember: this.remember
        });
        console.log('Login successful:', response.data);
      } catch (error) {
        console.error('Login failed:', error);
      }
    }
  }
}
</script>
