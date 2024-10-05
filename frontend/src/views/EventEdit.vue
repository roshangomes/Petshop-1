<template>
  <div class="max-w-xl mx-auto p-6 bg-white rounded shadow-md">
    <h1 class="text-2xl font-bold mb-4">Edit Event</h1>
    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-gray-700"
          >Title</label
        >
        <input
          type="text"
          v-model="title"
          id="title"
          class="mt-1 block w-full border border-gray-300 rounded p-2"
          required
        />
      </div>
      <div>
        <label for="description" class="block text-sm font-medium text-gray-700"
          >Description</label
        >
        <textarea
          v-model="description"
          id="description"
          class="mt-1 block w-full border border-gray-300 rounded p-2"
          required
        ></textarea>
      </div>
      <div>
        <label for="date" class="block text-sm font-medium text-gray-700"
          >Date</label
        >
        <input
          type="date"
          v-model="date"
          id="date"
          class="mt-1 block w-full border border-gray-300 rounded p-2"
          required
        />
      </div>
      <div>
        <label for="location" class="block text-sm font-medium text-gray-700"
          >Location</label
        >
        <input
          type="text"
          v-model="location"
          id="location"
          class="mt-1 block w-full border border-gray-300 rounded p-2"
          required
        />
      </div>
      <div>
        <label for="image" class="block text-sm font-medium text-gray-700"
          >Image</label
        >
        <input
          type="file"
          ref="file"
          @change="handleFileUpload"
          id="image"
          class="mt-1 block w-full text-gray-700 border border-gray-300 rounded p-2"
        />
      </div>
      <button
        type="submit"
        class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
      >
        Update Event
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      title: "",
      description: "",
      date: "",
      location: "",
      image: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.image = event.target.files[0];
    },
    async submitForm() {
      let formData = new FormData();
      if (this.image) {
        formData.append("image", this.image);
      }
      formData.append("title", this.title);
      formData.append("description", this.description);
      formData.append("date", this.date);
      formData.append("location", this.location);

      try {
        const url = ` /api/posts/events/${this.$route.params.id}/`; // Update event endpoint
        const response = await axios.put(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        console.log("Event updated:", response.data);
        this.$router.push("/events"); // Redirect to events page
      } catch (error) {
        console.error("Error updating event:", error);
        alert("Failed to update event. Please try again.");
      }
    },
    async fetchEvent() {
      try {
        const response = await axios.get(
          `/api/events/events/${this.$route.params.id}/`
        );
        const data = response.data; // Adjust based on your API response structure
        this.title = data.title;
        this.description = data.description;
        this.date = data.date;
        this.location = data.location;
      } catch (error) {
        console.error("Error fetching event:", error);
        alert("Failed to fetch event data.");
      }
    },
  },
  created() {
    if (this.$route.params.id) {
      this.fetchEvent(); // Fetch the event data if editing
    }
  },
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
