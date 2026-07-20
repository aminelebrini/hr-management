<template>
  <div class="min-h-screen bg-[#0a0a0a] flex">

    <!-- Sidebar -->
    <aside class="w-64 bg-[#0a0a0a] border-r border-zinc-800 flex flex-col fixed h-full">
      <div class="p-6 border-b border-zinc-800">
        <div class="flex items-center gap-3">
          <svg class="w-10 h-10" viewBox="0 0 56 56" fill="none">
            <rect width="56" height="56" rx="12" fill="white"/>
            <path d="M18 38V18h6l8 14V18h6v20h-6l-8-14v14h-6z" fill="#0a0a0a"/>
          </svg>
          <div>
            <h1 class="text-white font-bold text-sm">HR Management</h1>
            <p class="text-zinc-500 text-xs">Admin Panel</p>
          </div>
        </div>
      </div>

      <nav class="flex-1 p-4 space-y-1">
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 text-zinc-500 text-sm font-medium rounded-lg hover:text-white hover:bg-white/5 transition-colors">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1"/>
          </svg>
          Dashboard
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 bg-white/5 text-white text-sm font-medium rounded-lg">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>
          </svg>
          Employees
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 text-zinc-500 text-sm font-medium rounded-lg hover:text-white hover:bg-white/5 transition-colors">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          Attendance
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 text-zinc-500 text-sm font-medium rounded-lg hover:text-white hover:bg-white/5 transition-colors">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z"/>
          </svg>
          Leave Requests
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 text-zinc-500 text-sm font-medium rounded-lg hover:text-white hover:bg-white/5 transition-colors">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
          </svg>
          Settings
        </a>
      </nav>

      <div class="p-4 border-t border-zinc-800">
        <div class="flex items-center gap-3 px-3 py-2">
          <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
            <span class="text-zinc-400 text-xs font-medium">AD</span>
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-white text-sm font-medium truncate">Admin User</p>
            <p class="text-zinc-500 text-xs truncate">admin@hr.com</p>
          </div>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 ml-64">

      <!-- Header -->
      <header class="border-b border-zinc-800 px-8 py-5 flex items-center justify-between sticky top-0 bg-[#0a0a0a]/80 backdrop-blur-sm z-10">
        <div>
          <h2 class="text-white text-lg font-bold">Add Employee</h2>
          <p class="text-zinc-500 text-sm mt-0.5">Fill in the details to add a new employee.</p>
        </div>
        <a href="#" class="text-zinc-500 text-sm hover:text-white transition-colors flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
          </svg>
          Back to list
        </a>
      </header>

      <div class="p-8 max-w-3xl">

        <!-- Personal Information -->
        <div class="mb-8">
          <h3 class="text-white text-sm font-bold mb-5 flex items-center gap-2">
            <span class="w-6 h-6 rounded-full bg-white text-black text-xs font-bold flex items-center justify-center">1</span>
            Personal Information
          </h3>
          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-6">
            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Full Name</label>
                <input
                  type="text"
                  placeholder="Enter full name"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Email</label>
                <input
                  type="email"
                  placeholder="Enter email address"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Phone</label>
                <input
                  type="tel"
                  placeholder="Enter phone number"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">CIN</label>
                <input
                  type="text"
                  placeholder="Enter CIN number"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Date of Birth</label>
                <input
                  type="date"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Gender</label>
                <select class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-zinc-600 text-sm focus:outline-none focus:border-white transition-colors appearance-none cursor-pointer">
                  <option value="" class="bg-[#0a0a0a]">Select gender</option>
                  <option value="male" class="bg-[#0a0a0a] text-white">Male</option>
                  <option value="female" class="bg-[#0a0a0a] text-white">Female</option>
                </select>
              </div>
            </div>
          </div>
        </div>

        <!-- Employment Details -->
        <div class="mb-8">
          <h3 class="text-white text-sm font-bold mb-5 flex items-center gap-2">
            <span class="w-6 h-6 rounded-full bg-white text-black text-xs font-bold flex items-center justify-center">2</span>
            Employment Details
          </h3>
          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-6">
            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Department</label>
                <select class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-zinc-600 text-sm focus:outline-none focus:border-white transition-colors appearance-none cursor-pointer">
                  <option value="" class="bg-[#0a0a0a]">Select department</option>
                  <option value="engineering" class="bg-[#0a0a0a] text-white">Engineering</option>
                  <option value="marketing" class="bg-[#0a0a0a] text-white">Marketing</option>
                  <option value="hr" class="bg-[#0a0a0a] text-white">HR</option>
                  <option value="finance" class="bg-[#0a0a0a] text-white">Finance</option>
                  <option value="design" class="bg-[#0a0a0a] text-white">Design</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Position</label>
                <input
                  type="text"
                  placeholder="Enter position"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Role</label>
                <select class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-zinc-600 text-sm focus:outline-none focus:border-white transition-colors appearance-none cursor-pointer">
                  <option value="" class="bg-[#0a0a0a]">Select role</option>
                  <option value="admin" class="bg-[#0a0a0a] text-white">Admin</option>
                  <option value="employee" class="bg-[#0a0a0a] text-white">Employee</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Start Date</label>
                <input
                  type="date"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div class="col-span-2">
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Contract Type</label>
                <div class="flex gap-6 pt-2">
                  <label class="flex items-center gap-2 text-sm text-zinc-500 cursor-pointer select-none group">
                    <input type="radio" name="contract" value="cdi" class="peer sr-only" checked />
                    <span class="w-4 h-4 border border-zinc-700 rounded-full flex items-center justify-center peer-checked:border-white transition-colors group-hover:border-zinc-500">
                      <span class="w-2 h-2 rounded-full bg-white hidden peer-checked:block"></span>
                    </span>
                    CDI
                  </label>
                  <label class="flex items-center gap-2 text-sm text-zinc-500 cursor-pointer select-none group">
                    <input type="radio" name="contract" value="cdd" class="peer sr-only" />
                    <span class="w-4 h-4 border border-zinc-700 rounded-full flex items-center justify-center peer-checked:border-white transition-colors group-hover:border-zinc-500">
                      <span class="w-2 h-2 rounded-full bg-white hidden peer-checked:block"></span>
                    </span>
                    CDD
                  </label>
                  <label class="flex items-center gap-2 text-sm text-zinc-500 cursor-pointer select-none group">
                    <input type="radio" name="contract" value="stage" class="peer sr-only" />
                    <span class="w-4 h-4 border border-zinc-700 rounded-full flex items-center justify-center peer-checked:border-white transition-colors group-hover:border-zinc-500">
                      <span class="w-2 h-2 rounded-full bg-white hidden peer-checked:block"></span>
                    </span>
                    Stage
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Account -->
        <div class="mb-8">
          <h3 class="text-white text-sm font-bold mb-5 flex items-center gap-2">
            <span class="w-6 h-6 rounded-full bg-white text-black text-xs font-bold flex items-center justify-center">3</span>
            Account
          </h3>
          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-6">
            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Username</label>
                <input
                  type="text"
                  placeholder="Enter username"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-zinc-400 uppercase tracking-wider mb-2">Password</label>
                <input
                  type="password"
                  placeholder="Enter password"
                  class="w-full px-0 py-3 bg-transparent border-b border-zinc-800 text-white text-sm placeholder-zinc-600 focus:outline-none focus:border-white transition-colors"
                />
              </div>
            </div>
          </div>
        </div>

        <!-- Actions -->
        <div class="flex items-center justify-end gap-4">
          <a href="#" class="py-3 px-6 border border-zinc-800 text-zinc-400 text-sm font-medium rounded-lg hover:text-white hover:border-zinc-600 transition-colors">
            Cancel
          </a>
          <button class="py-3 px-6 bg-white text-black text-sm font-semibold rounded-lg hover:bg-zinc-200 transition-colors">
            Add Employee
          </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
export default {
  name: 'AddEmployeeView'
}
</script>
