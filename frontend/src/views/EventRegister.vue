<template>
  <div class="min-h-screen bg-gray-100 flex justify-center items-center">
    <div
      class="w-full max-w-2xl bg-white p-6 rounded-lg shadow-lg overflow-y-scroll h-[90vh]"
    >
      <h1 class="text-2xl font-bold mb-6 text-center">
        Event Registration Form
      </h1>

      <!-- Loading Indicator -->
      <div v-if="loading" class="text-center mb-4">
        Loading event details...
      </div>

      <!-- Error Message -->
      <div v-if="error" class="text-center text-red-500 mb-4">
        {{ error }}
      </div>

      <!-- Event Registration Form -->
      <form v-if="!loading && !error" @submit.prevent="submitForm">
        <!-- Full Name -->
        <div class="mb-4">
          <label for="fullName" class="block text-sm font-medium text-gray-700"
            >Full Name</label
          >
          <input
            v-model="form.fullName"
            type="text"
            id="fullName"
            class="mt-1 block w-full p-2 border rounded-lg"
            required
          />
        </div>

        <!-- Email -->
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700"
            >Email</label
          >
          <input
            v-model="form.email"
            type="email"
            id="email"
            class="mt-1 block w-full p-2 border rounded-lg"
            required
          />
        </div>

        <!-- Contact Number -->
        <div class="mb-4">
          <label for="contact" class="block text-sm font-medium text-gray-700"
            >Contact Number</label
          >
          <input
            v-model="form.contact"
            type="text"
            id="contact"
            class="mt-1 block w-full p-2 border rounded-lg"
            required
          />
        </div>

        <!-- Address -->
        <div class="mb-4">
          <label for="address" class="block text-sm font-medium text-gray-700"
            >Address</label
          >
          <textarea
            v-model="form.address"
            id="address"
            class="mt-1 block w-full p-2 border rounded-lg"
            rows="3"
          ></textarea>
        </div>

        <!-- Event Selection (Dynamic Event Title from API) -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700">Event</label>
          <input
            v-model="form.selectedEvent"
            type="text"
            class="mt-1 block w-full p-2 border rounded-lg"
            disabled
          />
        </div>

        <!-- Pet Type -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700"
            >Pet Type</label
          >
          <select
            v-model="form.petType"
            class="mt-1 block w-full p-2 border rounded-lg"
          >
            <option value="Dog">Dog</option>
            <option value="Cat">Cat</option>
            <option value="Bird">Bird</option>
          </select>
        </div>

        <!-- Pet Name -->
        <div class="mb-4">
          <label for="petName" class="block text-sm font-medium text-gray-700"
            >Pet Name</label
          >
          <input
            v-model="form.petName"
            type="text"
            id="petName"
            class="mt-1 block w-full p-2 border rounded-lg"
          />
        </div>

        <!-- Pet Date of Birth -->
        <div class="mb-4">
          <label for="petDob" class="block text-sm font-medium text-gray-700"
            >Pet Date of Birth</label
          >
          <input
            v-model="form.petDob"
            type="date"
            id="petDob"
            class="mt-1 block w-full p-2 border rounded-lg"
          />
        </div>

        <!-- Pet Vaccination Card Upload -->
        <div class="mb-4">
          <label
            for="vaccinationCard"
            class="block text-sm font-medium text-gray-700"
            >Upload Pet Vaccination Card</label
          >
          <input
            type="file"
            id="vaccinationCard"
            @change="handleFileUpload"
            class="mt-1 block w-full p-2 border rounded-lg"
          />
        </div>

        <!-- Agree to Terms -->
        <div class="mb-4">
          <label class="inline-flex items-center">
            <input
              v-model="form.agreeToTerms"
              type="checkbox"
              class="mr-2"
              required
            />
            I agree to the
            <a href="#" class="text-blue-500 underline">Terms and Conditions</a>
          </label>
        </div>

        <!-- Submit Button -->
        <div class="text-center">
          <button
            type="submit"
            class="bg-blue-600 text-white font-bold py-2 px-4 rounded-lg"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        fullName: "",
        email: "",
        contact: "",
        address: "",
        selectedEvent: "", // This will be populated with the event title from the backend
        petType: "",
        petName: "",
        petDob: "",
        vaccinationCard: null,
        agreeToTerms: false,
      },
      event: {}, // Event object to hold fetched details
      loading: true, // Loading state
      error: null, // Error message
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
            this.form.selectedEvent = response.data.title; // Populate the selectedEvent field with the event title
            this.loading = false; // Set loading to false after fetching
          } else {
            this.error = "Event not found."; // Handle case when event is not found
            this.loading = false;
          }
        })
        .catch((error) => {
          console.error("Error fetching event details:", error);
          this.error = "Failed to fetch event details."; // Set error message
          this.loading = false;
        });
    },

    handleFileUpload(event) {
      const file = event.target.files[0];
      this.form.vaccinationCard = file; // Save the file as a Blob object
    },
    submitForm() {
      const formData = new FormData();
      formData.append("fullName", this.form.fullName);
      formData.append("email", this.form.email);
      formData.append("contact", this.form.contact);
      formData.append("address", this.form.address);
      formData.append("selectedEvent", this.form.selectedEvent);
      formData.append("petType", this.form.petType);
      formData.append("petName", this.form.petName);
      formData.append("petDob", this.form.petDob);
      formData.append(
        "vaccinationCard",
        this.form.vaccinationCard,
        this.form.vaccinationCard.name
      );
      formData.append("agreeToTerms", this.form.agreeToTerms);

      // Retrieve the token from localStorage (or your preferred storage method)
      const token = localStorage.getItem("token"); // Ensure this line correctly retrieves the token

      axios
        .post("/api/posts/register/", formData, {
          headers: {
            Authorization: `Bearer ${token}`, // Add the token in the Authorization header
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log("Form submitted successfully:", response.data);
        })
        .catch((error) => {
          console.error("Error submitting form:", error.response.data);
        });
    },
  },
};
</script>

<style scoped>
.overflow-y-scroll {
  overflow-y: auto;
}
</style>
