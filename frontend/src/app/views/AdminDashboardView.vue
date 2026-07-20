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
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 bg-white/5 text-white text-sm font-medium rounded-lg">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1"/>
          </svg>
          Dashboard
        </a>
        <a href="#" class="flex items-center gap-3 px-3 py-2.5 text-zinc-500 text-sm font-medium rounded-lg hover:text-white hover:bg-white/5 transition-colors">
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
          <h2 class="text-white text-lg font-bold">Dashboard</h2>
          <p class="text-zinc-500 text-sm mt-0.5">Welcome back, here's what's happening today.</p>
        </div>
        <div class="flex items-center gap-4">
          <button class="relative p-2 text-zinc-500 hover:text-white transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
            </svg>
            <span class="absolute top-1.5 right-1.5 w-2 h-2 bg-white rounded-full"></span>
          </button>
          <a href="#" class="py-2 px-4 bg-white text-black text-sm font-semibold rounded-lg hover:bg-zinc-200 transition-colors">
            + Add Employee
          </a>
        </div>
      </header>

      <div class="p-8">

        <!-- Stats Cards -->
        <div class="grid grid-cols-4 gap-5 mb-8">
          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">Total Employees</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">142</p>
            <p class="text-zinc-500 text-xs mt-1">
              <span class="text-white">+12</span> this month
            </p>
          </div>

          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">Present Today</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">118</p>
            <p class="text-zinc-500 text-xs mt-1">
              <span class="text-white">83%</span> attendance rate
            </p>
          </div>

          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">On Leave</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">14</p>
            <p class="text-zinc-500 text-xs mt-1">
              <span class="text-white">5</span> pending requests
            </p>
          </div>

          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">Departments</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">8</p>
            <p class="text-zinc-500 text-xs mt-1">
              Across the company
            </p>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-5">

          <!-- Employee Table -->
          <div class="col-span-2 bg-[#0a0a0a] border border-zinc-800 rounded-xl">
            <div class="px-6 py-5 border-b border-zinc-800 flex items-center justify-between">
              <h3 class="text-white text-sm font-bold">Recent Employees</h3>
              <a href="#" class="text-zinc-500 text-xs hover:text-white transition-colors">View all</a>
            </div>
            <div class="overflow-x-auto">
              <table class="w-full">
                <thead>
                  <tr class="border-b border-zinc-800">
                    <th class="text-left px-6 py-3 text-zinc-500 text-xs font-medium uppercase tracking-wider">Employee</th>
                    <th class="text-left px-6 py-3 text-zinc-500 text-xs font-medium uppercase tracking-wider">Department</th>
                    <th class="text-left px-6 py-3 text-zinc-500 text-xs font-medium uppercase tracking-wider">Status</th>
                    <th class="text-left px-6 py-3 text-zinc-500 text-xs font-medium uppercase tracking-wider">Joined</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="border-b border-zinc-800/50 hover:bg-white/[0.02] transition-colors">
                    <td class="px-6 py-4">
                      <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                          <span class="text-zinc-400 text-xs font-medium">SA</span>
                        </div>
                        <div>
                          <p class="text-white text-sm font-medium">Sara Amrani</p>
                          <p class="text-zinc-500 text-xs">sara@company.com</p>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 text-zinc-400 text-sm">Engineering</td>
                    <td class="px-6 py-4">
                      <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-white/10 text-white">Active</span>
                    </td>
                    <td class="px-6 py-4 text-zinc-500 text-sm">Jan 15, 2026</td>
                  </tr>
                  <tr class="border-b border-zinc-800/50 hover:bg-white/[0.02] transition-colors">
                    <td class="px-6 py-4">
                      <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                          <span class="text-zinc-400 text-xs font-medium">YB</span>
                        </div>
                        <div>
                          <p class="text-white text-sm font-medium">Youssef Benani</p>
                          <p class="text-zinc-500 text-xs">youssef@company.com</p>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 text-zinc-400 text-sm">Marketing</td>
                    <td class="px-6 py-4">
                      <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-white/10 text-white">Active</span>
                    </td>
                    <td class="px-6 py-4 text-zinc-500 text-sm">Feb 3, 2026</td>
                  </tr>
                  <tr class="border-b border-zinc-800/50 hover:bg-white/[0.02] transition-colors">
                    <td class="px-6 py-4">
                      <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                          <span class="text-zinc-400 text-xs font-medium">FK</span>
                        </div>
                        <div>
                          <p class="text-white text-sm font-medium">Fatima Khalil</p>
                          <p class="text-zinc-500 text-xs">fatima@company.com</p>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 text-zinc-400 text-sm">HR</td>
                    <td class="px-6 py-4">
                      <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-zinc-700/50 text-zinc-400">On Leave</span>
                    </td>
                    <td class="px-6 py-4 text-zinc-500 text-sm">Mar 20, 2026</td>
                  </tr>
                  <tr class="border-b border-zinc-800/50 hover:bg-white/[0.02] transition-colors">
                    <td class="px-6 py-4">
                      <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                          <span class="text-zinc-400 text-xs font-medium">OE</span>
                        </div>
                        <div>
                          <p class="text-white text-sm font-medium">Omar El Idrissi</p>
                          <p class="text-zinc-500 text-xs">omar@company.com</p>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 text-zinc-400 text-sm">Finance</td>
                    <td class="px-6 py-4">
                      <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-white/10 text-white">Active</span>
                    </td>
                    <td class="px-6 py-4 text-zinc-500 text-sm">Apr 8, 2026</td>
                  </tr>
                  <tr class="hover:bg-white/[0.02] transition-colors">
                    <td class="px-6 py-4">
                      <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                          <span class="text-zinc-400 text-xs font-medium">NM</span>
                        </div>
                        <div>
                          <p class="text-white text-sm font-medium">Nadia Mansouri</p>
                          <p class="text-zinc-500 text-xs">nadia@company.com</p>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 text-zinc-400 text-sm">Design</td>
                    <td class="px-6 py-4">
                      <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-white/10 text-white">Active</span>
                    </td>
                    <td class="px-6 py-4 text-zinc-500 text-sm">May 12, 2026</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Right Column -->
          <div class="space-y-5">

            <!-- Leave Requests -->
            <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl">
              <div class="px-6 py-5 border-b border-zinc-800 flex items-center justify-between">
                <h3 class="text-white text-sm font-bold">Pending Requests</h3>
                <a href="#" class="text-zinc-500 text-xs hover:text-white transition-colors">View all</a>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                      <span class="text-zinc-400 text-xs font-medium">FK</span>
                    </div>
                    <div>
                      <p class="text-white text-sm font-medium">Fatima Khalil</p>
                      <p class="text-zinc-500 text-xs">Annual Leave</p>
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <button class="w-7 h-7 rounded-lg bg-white/10 flex items-center justify-center hover:bg-white/20 transition-colors">
                      <svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                      </svg>
                    </button>
                    <button class="w-7 h-7 rounded-lg bg-zinc-800 flex items-center justify-center hover:bg-zinc-700 transition-colors">
                      <svg class="w-3.5 h-3.5 text-zinc-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                      </svg>
                    </button>
                  </div>
                </div>
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                      <span class="text-zinc-400 text-xs font-medium">SA</span>
                    </div>
                    <div>
                      <p class="text-white text-sm font-medium">Sara Amrani</p>
                      <p class="text-zinc-500 text-xs">Sick Leave</p>
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <button class="w-7 h-7 rounded-lg bg-white/10 flex items-center justify-center hover:bg-white/20 transition-colors">
                      <svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                      </svg>
                    </button>
                    <button class="w-7 h-7 rounded-lg bg-zinc-800 flex items-center justify-center hover:bg-zinc-700 transition-colors">
                      <svg class="w-3.5 h-3.5 text-zinc-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                      </svg>
                    </button>
                  </div>
                </div>
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                      <span class="text-zinc-400 text-xs font-medium">OE</span>
                    </div>
                    <div>
                      <p class="text-white text-sm font-medium">Omar El Idrissi</p>
                      <p class="text-zinc-500 text-xs">Personal Day</p>
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <button class="w-7 h-7 rounded-lg bg-white/10 flex items-center justify-center hover:bg-white/20 transition-colors">
                      <svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                      </svg>
                    </button>
                    <button class="w-7 h-7 rounded-lg bg-zinc-800 flex items-center justify-center hover:bg-zinc-700 transition-colors">
                      <svg class="w-3.5 h-3.5 text-zinc-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Department Breakdown -->
            <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl">
              <div class="px-6 py-5 border-b border-zinc-800">
                <h3 class="text-white text-sm font-bold">Departments</h3>
              </div>
              <div class="p-6 space-y-4">
                <div>
                  <div class="flex items-center justify-between mb-2">
                    <span class="text-zinc-400 text-sm">Engineering</span>
                    <span class="text-zinc-500 text-xs">42</span>
                  </div>
                  <div class="w-full h-1 bg-zinc-800 rounded-full">
                    <div class="h-1 bg-white rounded-full" style="width: 30%"></div>
                  </div>
                </div>
                <div>
                  <div class="flex items-center justify-between mb-2">
                    <span class="text-zinc-400 text-sm">Marketing</span>
                    <span class="text-zinc-500 text-xs">28</span>
                  </div>
                  <div class="w-full h-1 bg-zinc-800 rounded-full">
                    <div class="h-1 bg-white rounded-full" style="width: 20%"></div>
                  </div>
                </div>
                <div>
                  <div class="flex items-center justify-between mb-2">
                    <span class="text-zinc-400 text-sm">HR</span>
                    <span class="text-zinc-500 text-xs">18</span>
                  </div>
                  <div class="w-full h-1 bg-zinc-800 rounded-full">
                    <div class="h-1 bg-white rounded-full" style="width: 13%"></div>
                  </div>
                </div>
                <div>
                  <div class="flex items-center justify-between mb-2">
                    <span class="text-zinc-400 text-sm">Finance</span>
                    <span class="text-zinc-500 text-xs">24</span>
                  </div>
                  <div class="w-full h-1 bg-zinc-800 rounded-full">
                    <div class="h-1 bg-white rounded-full" style="width: 17%"></div>
                  </div>
                </div>
                <div>
                  <div class="flex items-center justify-between mb-2">
                    <span class="text-zinc-400 text-sm">Design</span>
                    <span class="text-zinc-500 text-xs">30</span>
                  </div>
                  <div class="w-full h-1 bg-zinc-800 rounded-full">
                    <div class="h-1 bg-white rounded-full" style="width: 21%"></div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
export default {
  name: 'AdminDashboardView'
}
</script>
