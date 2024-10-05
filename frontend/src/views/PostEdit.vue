<template>
  <div v-if="post" class="max-w-4xl mx-auto mt-10 bg-white shadow-md rounded p-6">
    <h2 class="text-2xl font-bold mb-6">Edit Post</h2>
    <form @submit.prevent="updatePost">
      <!-- Title -->
      <div class="mb-4">
        <label for="title" class="block text-sm font-medium text-gray-700">Title</label>
        <input
          v-model="post.title"
          :placeholder="originalPost.title || 'Enter the title'"
          type="text"
          id="title"
          class="mt-1 block w-full border-gray-300 rounded-md"
        />
      </div>

      <!-- Description -->
      <div class="mb-4">
        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
        <textarea
          v-model="post.description"
          :placeholder="originalPost.description || 'Enter the description'"
          id="description"
          class="mt-1 block w-full border-gray-300 rounded-md"
        ></textarea>
      </div>

      <!-- Contact Information -->
      <div class="mb-4">
        <label for="contact_information" class="block text-sm font-medium text-gray-700">Contact Information</label>
        <textarea
          v-model="post.contact_information"
          :placeholder="originalPost.contact_information || 'Enter contact information'"
          id="contact_information"
          class="mt-1 block w-full border-gray-300 rounded-md"
        ></textarea>
      </div>

      <!-- Price -->
      <div class="mb-4">
        <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
        <input
          v-model="post.price"
          :placeholder="originalPost.price || 'Enter the price'"
          type="number"
          step="0.01"
          id="price"
          class="mt-1 block w-full border-gray-300 rounded-md"
        />
      </div>

      <!-- Category -->
      <div class="mb-4">
        <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
        <input
          v-model="post.category"
          :placeholder="originalPost.category || 'Enter the category'"
          type="text"
          id="category"
          class="mt-1 block w-full border-gray-300 rounded-md"
        />
      </div>

      <!-- Breed, Color, Age, Gender -->
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label for="breed" class="block text-sm font-medium text-gray-700">Breed</label>
          <input
            v-model="post.breed"
            :placeholder="originalPost.breed || 'Enter breed'"
            type="text"
            id="breed"
            class="mt-1 block w-full border-gray-300 rounded-md"
          />
        </div>
        <div>
          <label for="color" class="block text-sm font-medium text-gray-700">Color</label>
          <input
            v-model="post.color"
            :placeholder="originalPost.color || 'Enter color'"
            type="text"
            id="color"
            class="mt-1 block w-full border-gray-300 rounded-md"
          />
        </div>
        <div>
          <label for="age" class="block text-sm font-medium text-gray-700">Age (Months)</label>
          <input
            v-model="post.age"
            :placeholder="originalPost.age || 'Enter age'"
            type="number"
            id="age"
            class="mt-1 block w-full border-gray-300 rounded-md"
          />
        </div>
        <div>
          <label for="gender" class="block text-sm font-medium text-gray-700">Gender</label>
          <select v-model="post.gender" id="gender" class="mt-1 block w-full border-gray-300 rounded-md">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
      </div>

      <!-- Vaccinated, Microchipped, Trained, Health Certificate -->
      <div class="grid grid-cols-2 gap-4 mt-4">
        <div>
          <label for="vaccinated" class="block text-sm font-medium text-gray-700">Vaccinated</label>
          <input v-model="post.vaccinated" type="checkbox" id="vaccinated" />
        </div>
        <div>
          <label for="microchipped" class="block text-sm font-medium text-gray-700">Microchipped</label>
          <input v-model="post.microchipped" type="checkbox" id="microchipped" />
        </div>
        <div>
          <label for="trained" class="block text-sm font-medium text-gray-700">Trained</label>
          <input v-model="post.trained" type="checkbox" id="trained" />
        </div>
        <div>
          <label for="health_certificate" class="block text-sm font-medium text-gray-700">Health Certificate</label>
          <input v-model="post.health_certificate" type="checkbox" id="health_certificate" />
        </div>
      </div>

      <!-- Body -->
      <div class="mt-4">
        <label for="body" class="block text-sm font-medium text-gray-700">Additional Information</label>
        <textarea
          v-model="post.body"
          :placeholder="originalPost.body || 'Enter additional information'"
          id="body"
          class="mt-1 block w-full border-gray-300 rounded-md"
        ></textarea>
      </div>

      <!-- Submit Button -->
      <div class="mt-6">
        <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded">Update Post</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EditPost",
  data() {
    return {
      post: {
        title: "",
        description: "",
        contact_information: "",
        price: 0,
        category: "",
        breed: "",
        color: "",
        age: null,
        vaccinated: false,
        gender: "",
        weight: null,
        microchipped: false,
        trained: false,
        health_certificate: false,
        body: "",
      },
      originalPost: {}, // For storing the original fetched data
      errors: [],
      errorMessage: "",
    };
  },
  methods: {
    async fetchPost() {
      try {
        const response = await axios.get(`/api/posts/${this.$route.params.id}/`);
        const data = response.data.post;
        this.originalPost = { ...data }; // Store the fetched data in originalPost
      } catch (error) {
        this.errorMessage = "Error fetching post data.";
        console.error("Error fetching post:", error.response ? error.response.data : error.message);
      }
    },

    async updatePost() {
  this.errors = [];
  
  // Check if title and description are empty
  if (this.post.title === '') this.errors.push('Title is required');
  if (this.post.description === '') this.errors.push('Description is required');

  // Proceed only if there are no errors
  if (this.errors.length === 0) {
    try {
      const updatedPost = { ...this.post };

      // Convert string values back to booleans if needed
      updatedPost.vaccinated = updatedPost.vaccinated === true; // No need to convert from string
      updatedPost.microchipped = updatedPost.microchipped === true;
      updatedPost.trained = updatedPost.trained === true;
      updatedPost.health_certificate = updatedPost.health_certificate === true;

      const response = await axios.put(`/api/posts/${this.$route.params.id}/edit/`, updatedPost);

      alert("Post updated successfully");
      this.$router.push(`/${this.$route.params.id}`);
    } catch (error) {
      console.error("Error updating post:", error.response.data);
      alert("Error updating post");
    }
  }

    },
  },
  created() {
    this.fetchPost();
  },
};
</script>
