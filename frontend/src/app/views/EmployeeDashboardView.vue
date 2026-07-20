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
            <p class="text-zinc-500 text-xs">Employee Portal</p>
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
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
          My Profile
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
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
          </svg>
          Payslips
        </a>
      </nav>

      <div class="p-4 border-t border-zinc-800">
        <div class="flex items-center gap-3 px-3 py-2">
          <div class="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
            <span class="text-zinc-400 text-xs font-medium">SA</span>
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-white text-sm font-medium truncate">Sara Amrani</p>
            <p class="text-zinc-500 text-xs truncate">sara@company.com</p>
          </div>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 ml-64">

      <!-- Header -->
      <header class="border-b border-zinc-800 px-8 py-5 flex items-center justify-between sticky top-0 bg-[#0a0a0a]/80 backdrop-blur-sm z-10">
        <div>
          <h2 class="text-white text-lg font-bold">My Dashboard</h2>
          <p class="text-zinc-500 text-sm mt-0.5">Welcome back, Sara. Here's your overview.</p>
        </div>
        <div class="flex items-center gap-4">
          <button class="relative p-2 text-zinc-500 hover:text-white transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
            </svg>
            <span class="absolute top-1.5 right-1.5 w-2 h-2 bg-white rounded-full"></span>
          </button>
          <a href="#" class="py-2 px-4 bg-white text-black text-sm font-semibold rounded-lg hover:bg-zinc-200 transition-colors">
            Request Leave
          </a>
        </div>
      </header>

      <div class="p-8">

        <!-- Stats Cards -->
        <div class="grid grid-cols-4 gap-5 mb-8">
          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">Days Worked</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">22</p>
            <p class="text-zinc-500 text-xs mt-1">Out of 24 working days</p>
          </div>

          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">Leave Balance</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">15</p>
            <p class="text-zinc-500 text-xs mt-1">Days remaining</p>
          </div>

          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">Late Arrivals</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">2</p>
            <p class="text-zinc-500 text-xs mt-1">This month</p>
          </div>

          <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl p-5 hover:border-zinc-700 transition-colors">
            <div class="flex items-center justify-between mb-4">
              <span class="text-zinc-500 text-xs font-medium uppercase tracking-wider">Pending Requests</span>
              <svg class="w-4 h-4 text-zinc-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
              </svg>
            </div>
            <p class="text-white text-2xl font-bold">1</p>
            <p class="text-zinc-500 text-xs mt-1">Awaiting approval</p>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-5">

          <!-- Today's Schedule -->
          <div class="col-span-2 bg-[#0a0a0a] border border-zinc-800 rounded-xl">
            <div class="px-6 py-5 border-b border-zinc-800 flex items-center justify-between">
              <h3 class="text-white text-sm font-bold">Today's Schedule</h3>
              <span class="text-zinc-500 text-xs">Mon, Jul 20 2026</span>
            </div>
            <div class="p-6 space-y-4">
              <div class="flex items-start gap-4 p-4 rounded-lg border border-zinc-800/50 hover:border-zinc-800 transition-colors">
                <div class="w-1 text-white rounded-full min-h-[3rem] bg-white"></div>
                <div class="flex-1">
                  <p class="text-white text-sm font-medium">Team Standup</p>
                  <p class="text-zinc-500 text-xs mt-1">09:00 - 09:30 · Engineering</p>
                </div>
                <span class="text-zinc-500 text-xs">Completed</span>
              </div>
              <div class="flex items-start gap-4 p-4 rounded-lg border border-zinc-800/50 hover:border-zinc-800 transition-colors">
                <div class="w-1 text-white rounded-full min-h-[3rem] bg-zinc-700"></div>
                <div class="flex-1">
                  <p class="text-white text-sm font-medium">Sprint Planning</p>
                  <p class="text-zinc-500 text-xs mt-1">10:00 - 11:30 · Conference Room B</p>
                </div>
                <span class="text-white text-xs bg-white/10 px-2.5 py-0.5 rounded-full">In Progress</span>
              </div>
              <div class="flex items-start gap-4 p-4 rounded-lg border border-zinc-800/50 hover:border-zinc-800 transition-colors">
                <div class="w-1 text-white rounded-full min-h-[3rem] bg-zinc-800"></div>
                <div class="flex-1">
                  <p class="text-white text-sm font-medium">Code Review</p>
                  <p class="text-zinc-500 text-xs mt-1">14:00 - 15:00 · Online</p>
                </div>
                <span class="text-zinc-600 text-xs">Upcoming</span>
              </div>
              <div class="flex items-start gap-4 p-4 rounded-lg border border-zinc-800/50 hover:border-zinc-800 transition-colors">
                <div class="w-1 text-white rounded-full min-h-[3rem] bg-zinc-800"></div>
                <div class="flex-1">
                  <p class="text-white text-sm font-medium">1-on-1 with Manager</p>
                  <p class="text-zinc-500 text-xs mt-1">16:00 - 16:30 · Manager's Office</p>
                </div>
                <span class="text-zinc-600 text-xs">Upcoming</span>
              </div>
            </div>
          </div>

          <!-- Right Column -->
          <div class="space-y-5">

            <!-- Profile Card -->
            <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl">
              <div class="px-6 py-5 border-b border-zinc-800">
                <h3 class="text-white text-sm font-bold">My Info</h3>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex justify-center mb-2">
                  <div class="w-16 h-16 rounded-full bg-zinc-800 flex items-center justify-center">
                    <span class="text-zinc-400 text-lg font-medium">SA</span>
                  </div>
                </div>
                <div class="text-center mb-4">
                  <p class="text-white text-sm font-bold">Sara Amrani</p>
                  <p class="text-zinc-500 text-xs mt-0.5">Senior Engineer</p>
                </div>
                <div class="space-y-3">
                  <div class="flex items-center justify-between">
                    <span class="text-zinc-500 text-xs">Department</span>
                    <span class="text-zinc-400 text-xs">Engineering</span>
                  </div>
                  <div class="flex items-center justify-between">
                    <span class="text-zinc-500 text-xs">Manager</span>
                    <span class="text-zinc-400 text-xs">Youssef B.</span>
                  </div>
                  <div class="flex items-center justify-between">
                    <span class="text-zinc-500 text-xs">Joined</span>
                    <span class="text-zinc-400 text-xs">Jan 15, 2026</span>
                  </div>
                  <div class="flex items-center justify-between">
                    <span class="text-zinc-500 text-xs">Employee ID</span>
                    <span class="text-zinc-400 text-xs">EMP-0042</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Recent Activity -->
            <div class="bg-[#0a0a0a] border border-zinc-800 rounded-xl">
              <div class="px-6 py-5 border-b border-zinc-800">
                <h3 class="text-white text-sm font-bold">Recent Activity</h3>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex items-start gap-3">
                  <div class="w-1.5 h-1.5 rounded-full bg-white mt-2 flex-shrink-0"></div>
                  <div>
                    <p class="text-zinc-400 text-xs">Checked in at <span class="text-white">08:57 AM</span></p>
                    <p class="text-zinc-600 text-xs mt-0.5">Today</p>
                  </div>
                </div>
                <div class="flex items-start gap-3">
                  <div class="w-1.5 h-1.5 rounded-full bg-zinc-700 mt-2 flex-shrink-0"></div>
                  <div>
                    <p class="text-zinc-400 text-xs">Leave request <span class="text-white">approved</span></p>
                    <p class="text-zinc-600 text-xs mt-0.5">Yesterday</p>
                  </div>
                </div>
                <div class="flex items-start gap-3">
                  <div class="w-1.5 h-1.5 rounded-full bg-zinc-700 mt-2 flex-shrink-0"></div>
                  <div>
                    <p class="text-zinc-400 text-xs">Payslip for <span class="text-white">June</span> downloaded</p>
                    <p class="text-zinc-600 text-xs mt-0.5">Jul 5, 2026</p>
                  </div>
                </div>
                <div class="flex items-start gap-3">
                  <div class="w-1.5 h-1.5 rounded-full bg-zinc-700 mt-2 flex-shrink-0"></div>
                  <div>
                    <p class="text-zinc-400 text-xs">Profile <span class="text-white">updated</span></p>
                    <p class="text-zinc-600 text-xs mt-0.5">Jul 1, 2026</p>
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
  name: 'EmployeeDashboardView'
}
</script>
