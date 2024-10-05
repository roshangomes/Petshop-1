<template>
  <div class="p-2 bg-gray-100 min-h-screen">
    <h1 class="text-3xl font-bold text-center mt-2 mb-5">{{ event.title }}</h1>

    <div
      class="bg-white p-4 rounded-lg shadow-lg flex flex-col justify-between h-full"
    >
      <div class="grid grid-cols-2 gap-6">
        <div>
          <div v-if="loading">Loading...</div>
          <div v-if="error" class="text-red-500">{{ error }}</div>

          <div v-if="event.attachments.length">
            <div v-for="attachment in event.attachments" :key="attachment.id">
              <img
                :src="attachment.image_url"
                alt="Event Attachment"
                class="w-full h-90 object-cover rounded-lg"
              />
            </div>
            <div class="grid grid-cols-2 gap-4 text-gray-700 mb-4">
              <!-- Date Section -->
              <div class="flex items-center">
                <i class="fas fa-calendar-alt mr-2"></i>
                <p>{{ formatDate(event.created_at) }}</p>
              </div>

              <!-- Location Section -->
              <div class="flex items-center">
                <i class="fas fa-map-marker-alt mr-2"></i>
                <p>{{ event.location }}</p>
              </div>

              <!-- Time Section -->
              <div class="flex items-center">
                <i class="fas fa-clock mr-2"></i>
                <p>{{ event.time }}</p>
                <!-- Assuming there's a 'time' field for the event -->
              </div>

              <!-- Contact Section -->
              <div class="flex items-center">
                <i class="fas fa-phone mr-2"></i>
                <p>{{ event.contact }}</p>
              </div>
            </div>

            <!-- "Book Now" Button at the Bottom -->
            <div class="mt-6">
              <router-link
                :to="{ name: 'eventregister', params: { eventId: event.id } }"
              >
                <button
                  class="bg-red-600 text-white font-bold py-3 w-full text-center"
                >
                  Book Now
                </button>
              </router-link>
            </div>
          </div>

          <div v-else>
            <img
              src="path/to/placeholder-image.jpg"
              alt="No Image Available"
              class="w-full h-90 object-cover rounded-lg"
            />
          </div>
        </div>

        <div
          class="bg-white p-4 rounded-lg shadow-lg flex flex-col justify-between h-full"
        >
          <div>
            <div
              class="flex justify-between p-4 bg-gray-800 text-white rounded-lg mb-5"
            >
              <div class="flex items-center">
                <i class="fas fa-map-marker mr-2"></i>
                <div>
                  <h2 class="text-lg font-semibold">Location</h2>
                  <p class="text-sm">{{ event.location }}</p>
                </div>
              </div>

              <div class="flex items-center">
                <i class="fas fa-calendar-alt mr-2"></i>
                <div>
                  <h2 class="text-lg font-semibold">Posted On</h2>
                  <p class="text-sm">{{ formatDate(event.created_at) }}</p>
                </div>
              </div>

              <div class="flex items-center">
                <i class="fas fa-user mr-2"></i>
                <div>
                  <h2 class="text-lg font-semibold">Posted By</h2>
                  <p class="text-sm">{{ event.organizer_id }}</p>
                </div>
              </div>
            </div>

            <h2 class="text-xl font-bold mb-2">About</h2>
            <p>{{ event.description }}</p>
          </div>

          <!-- Buttons stay at the bottom -->
          <div class="mt-4 flex space-x-4">
            <button
              class="bg-blue-500 text-white font-bold py-2 px-4 rounded-lg"
            >
              Bookmark
            </button>
            <button
              class="bg-gray-500 text-white font-bold py-2 px-4 rounded-lg"
            >
              Contact Event Host
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EventDetails",
  data() {
    return {
      event: {}, // Event object to hold fetched details
      loading: true, // Loading state to show a loading indicator if needed
      error: null, // Error message for displaying any errors
    };
  },
  created() {
    this.fetchEventDetails();
  },
  methods: {
    fetchEventDetails() {
      const eventId = this.$route.params.id; // Get the event ID from the route
      console.log("Event ID:", eventId); // Log the event ID for debugging

      axios
        .get(`/api/posts/events/${eventId}`)
        .then((response) => {
          if (response.data) {
            this.event = response.data; // Assuming response.data contains the event details directly
            this.loading = false; // Set loading to false after fetching
          } else {
            this.error = "Event not found."; // Handle case when event is not found
            this.loading = false; // Set loading to false in case of error
          }
        })
        .catch((error) => {
          console.error("Error fetching event details:", error);
          this.error = "Failed to fetch event details."; // Set an error message
          this.loading = false; // Set loading to false in case of error
        });
    },

    formatDate(dateString) {
      const options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },

    // Method to navigate to event registration page
    bookNow() {
      const eventId = this.$route.params.id; // Get the event ID from the route
      this.$router.push({ name: "eventregister", params: { eventId } }); // Navigate to the eventregister route with eventId
    },
  },
};
</script>

<style scoped>
/* Add any additional styles here if needed */
</style>
