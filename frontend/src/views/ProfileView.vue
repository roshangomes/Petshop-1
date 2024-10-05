<template>
  <!-- <div class="max-w-7xl mx-auto p-6 mb-6 mt-4 bg-white border border-gray-200 rounded-lg"> -->
  <!-- User Info Section -->
  <div
    class="max-w-7xl mx-auto p-6 mb-6 mt-4 bg-white border border-gray-200 rounded-lg"
  >
    <div class="flex flex-col items-center mb-4">
      <div class="flex-shrink-0 mb-4">
        <img :src="user.get_avatar" class="w-32 h-32 rounded-full" />
      </div>
      <p class="text-xl font-semibold mb-2">
        <strong>{{ user.name }}</strong>
      </p>
    </div>

    <div class="flex flex-col items-center mb-4" v-if="user.id">
      <div class="flex space-x-10 mb-4">
        <RouterLink
          :to="{ name: 'friends', params: { id: user.id } }"
          class="text-sm text-gray-500"
        >
          {{ user.friends_count }} Buddies
        </RouterLink>
        <p class="text-sm text-gray-500">{{ user.posts_count }} posts</p>
      </div>

      <div class="flex space-x-4 mb-4">
        <button
          class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
          @click="sendFriendshipRequest"
          v-if="userStore.user.id !== user.id"
        >
          Send Buddy request
        </button>
        <button
          class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
          @click="sendDirectMessage"
          v-if="userStore.user.id !== user.id"
        >
          Send direct message
        </button>
        <RouterLink
          class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
          to="/profile/edit"
          v-if="userStore.user.id === user.id"
        >
          Edit profile
        </RouterLink>
        <button
          class="py-2 px-4 bg-red-600 text-sm text-white rounded-lg"
          @click="logout"
          v-if="userStore.user.id === user.id"
        >
          Log out
        </button>
        <RouterLink
          to="/feedform"
          class="py-2 px-4 bg-green-500 text-sm text-white rounded-lg"
        >
          Create Ad
        </RouterLink>
      </div>
    </div>
  </div>

  <!-- Toggle Buttons for Posts, Events, and Registered Events -->
  <div class="flex flex-row justify-center space-x-2 mb-4">
    <button
      @click="toggleView('posts')"
      :class="{
        'bg-blue-500 text-white': currentView === 'posts',
        'bg-gray-200 text-gray-700': currentView !== 'posts',
      }"
      class="py-2 px-4 rounded-lg"
    >
      Posts
    </button>
    <button
      @click="toggleView('events')"
      :class="{
        'bg-blue-500 text-white': currentView === 'events',
        'bg-gray-200 text-gray-700': currentView !== 'events',
      }"
      class="py-2 px-4 rounded-lg"
    >
      Events
    </button>
    <button
      @click="toggleView('registeredEvents')"
      :class="{
        'bg-blue-500 text-white': currentView === 'registeredEvents',
        'bg-gray-200 text-gray-700': currentView !== 'registeredEvents',
      }"
      class="py-2 px-4 rounded-lg"
    >
      Registered Events
    </button>
  </div>

  <!-- Posts Section -->
  <div
    class="max-w-9xl mx-auto p-6 mb-10 bg-white rounded shadow-md min-h-[400px]"
    v-if="currentView === 'posts'"
  >
    <h1 class="text-2xl font-bold mb-4">Posts</h1>
    <div v-if="posts.length">
      <table class="min-w-full bg-white border border-gray-200 rounded-lg">
        <thead>
          <tr class="w-full bg-gray-100 border-b border-gray-200">
            <th class="px-6 py-3 text-left text-gray-600 font-medium">S.NO</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Ad Id</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Image</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Title</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Description
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Published
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Interests
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(post, index) in posts"
            :key="post.id"
            class="border-b border-gray-200"
          >
            <td class="px-6 py-4 text-gray-500">{{ index + 1 }}</td>
            <td class="px-6 py-4 text-gray-800">{{ post.id.slice(-4) }}</td>
            <td class="px-5 py-4 text-gray-500">
              <div class="flex flex-wrap gap-2">
                <router-link
                  v-for="image in post.attachments"
                  :key="image.id"
                  :to="/${post.id}/"
                  class="block"
                >
                  <img
                    :src="image.get_image"
                    class="w-32 h-32 object-cover rounded-lg cursor-pointer"
                  />
                </router-link>
              </div>
            </td>
            <td class="px-6 py-4 text-gray-800">{{ post.title }}</td>
            <td class="px-6 py-4 text-gray-600">{{ post.description }}</td>
            <td class="px-6 py-4 text-gray-500">
              {{ post.created_at_formatted }} Ago
            </td>
            <td class="px-6 py-4 text-gray-500">
              {{ post.likes_count }} Likes, {{ post.comments_count }} Comments
            </td>
            <td class="px-6 py-4 text-gray-500">
              <div class="flex items-center space-x-2">
                <button
                  @click="editPost(post.id)"
                  class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600"
                  v-if="userStore.user.id === post.created_by.id"
                >
                  Edit
                </button>
                <button
                  @click="deletePost(post.id)"
                  class="bg-red-500 text-white font-bold py-2 px-4 rounded hover:bg-red-600"
                  v-if="userStore.user.id === post.created_by.id"
                >
                  Delete
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p class="text-gray-700">No posts available.</p>
    </div>
  </div>
  <!-- Events Section -->
  <div
    v-if="currentView === 'events'"
    class="max-w-9xl mx-auto p-6 mb-10 bg-white rounded shadow-md min-h-[400px]"
  >
    <h1 class="text-2xl font-bold mb-4">Events</h1>
    <div v-if="events.length">
      <div class="overflow-x-auto">
        <!-- Add scroll on small screens -->
        <table class="min-w-full bg-white border border-gray-200 rounded-lg">
          <thead>
            <tr class="w-full bg-gray-100 border-b border-gray-200">
              <th class="px-6 py-3 text-left text-gray-600 font-medium">
                S.NO
              </th>
              <th class="px-6 py-3 text-left text-gray-600 font-medium">
                Event Id
              </th>
              <th class="px-6 py-3 text-left text-gray-600 font-medium">
                Title
              </th>
              <th class="px-6 py-3 text-left text-gray-600 font-medium">
                Date
              </th>
              <th class="px-6 py-3 text-left text-gray-600 font-medium">
                Location
              </th>
              <th class="px-6 py-3 text-left text-gray-600 font-medium">
                Actions
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(event, index) in events"
              :key="event.id"
              class="border-b border-gray-200"
            >
              <td class="px-6 py-4 text-gray-500">{{ index + 1 }}</td>
              <td class="px-6 py-4 text-gray-800">{{ event.id.slice(-4) }}</td>
              <td class="px-6 py-4 text-gray-800">{{ event.title }}</td>
              <td class="px-6 py-4 text-gray-500">{{ event.date }}</td>
              <td class="px-6 py-4 text-gray-500">{{ event.location }}</td>
              <td class="px-6 py-4 text-gray-500">
                <div class="flex items-center space-x-2">
                  <!-- Show edit/delete buttons if the user is the event creator -->
                  <button
                    @click="editEvent(event.id)"
                    class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600"
                    aria-label="Edit event"
                  >
                    Edit
                  </button>
                  <button
                    @click="deleteEvent(event.id)"
                    class="bg-red-500 text-white font-bold py-2 px-4 rounded hover:bg-red-600"
                    aria-label="Delete event"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else>
      <p class="text-gray-700">No events available.</p>
    </div>
  </div>

  <!-- Registered Events Section -->
  <div
    class="max-w-9xl mx-auto p-6 mb-10 bg-white rounded shadow-md min-h-[400px]"
    v-else-if="currentView === 'registeredEvents'"
  >
    <h1 class="text-2xl font-bold mb-4">Registered Events</h1>
    <div v-if="registeredEvents.length">
      <table class="min-w-full bg-white border border-gray-200 rounded-lg">
        <thead>
          <tr class="w-full bg-gray-100 border-b border-gray-200">
            <th class="px-6 py-3 text-left text-gray-600 font-medium">S.NO</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Event Id
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Title</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Date</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Location
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(event, index) in registeredEvents"
            :key="event.id"
            class="border-b border-gray-200"
          >
            <td class="px-6 py-4 text-gray-500">{{ index + 1 }}</td>
            <td class="px-6 py-4 text-gray-800">{{ event.id.slice(-4) }}</td>
            <td class="px-6 py-4 text-gray-800">{{ event.title }}</td>
            <td class="px-6 py-4 text-gray-500">{{ event.date }}</td>
            <td class="px-6 py-4 text-gray-500">{{ event.location }}</td>
            <td class="px-6 py-4 text-gray-500">
              <button
                @click="unregisterEvent(event.id)"
                class="bg-red-500 text-white font-bold py-2 px-4 rounded hover:bg-red-600"
              >
                Unregister
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p class="text-gray-700">No registered events.</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FeedItem from "../components/FeedItem.vue";
import { useUserStore } from "@/stores/user";
import { useToastStore } from "@/stores/toast";
import { RouterLink } from "vue-router";
import FeedForm from "./FeedForm.vue";

export default {
  name: "FeedView",

  setup() {
    const userStore = useUserStore();
    const toastStore = useToastStore();

    return {
      userStore,
      toastStore,
    };
  },

  components: {
    FeedItem,
    FeedForm,
  },

  data() {
    return {
      currentView: "posts", // Default view set to posts
      posts: [],
      events: [], // Events will be fetched
      registeredEvents: [], // Registered events will be fetched
      user: {
        id: "",
      },
      // Form fields for posting
      body: "",
      url: null,
      title: "",
      description: "",
      contact_information: "",
      price: "",
      category: "",
      breed: "",
      color: "",
      age: null,
      vaccinated: "",
      gender: "",
      weight: null,
      microchipped: "",
      trained: "",
      health_certificate: "",
    };
  },

  mounted() {
    this.getFeed();
    this.fetchEvents();
    this.fetchRegisteredEvents();
    // Fetch events on load
  },

  watch: {
    "$route.params.id": {
      handler: function () {
        this.getFeed();
        this.fetchEvents();
        this.fetchRegisteredEvents(); // Refetch events when user ID changes
      },
      deep: true,
      immediate: true,
    },
  },

  methods: {
    // Toggle between posts and events view
    toggleView(view) {
      this.currentView = view;
      if (view === "events") {
        this.getEvents(); // Fetch events created by the user
      } else if (view === "registeredEvents") {
        this.fetchRegisteredEvents(); // Fetch events the user registered for
      }
    },

    // Fetch user's posts
    getFeed() {
      axios
        .get(`/api/posts/profile/${this.$route.params.id}/`)
        .then((response) => {
          this.posts = response.data.posts;
          this.user = response.data.user;
          this.user.posts_count = this.posts.length;
        })
        .catch((error) => {
          console.error("Error fetching posts:", error);
        });
    },
    fetchEvents() {
      axios
        .get("/api/posts/events/")
        .then((response) => {
          const currentUserId = this.userStore.user.id; // Get the current user's ID

          // Log the current user ID and the organizer IDs from the response
          console.log("Current User ID:", currentUserId);
          console.log("Events Response:", response.data);

          // Filter events where the current user is the organizer
          this.events = response.data.filter((event) => {
            console.log("Event Organizer ID:", event.organizer); // Log the organizer ID for each event
            return event.organizer === currentUserId; // Compare as strings
          });

          if (!this.events.length) {
            console.log("No events found for the current user.");
          } else {
            console.log("Filtered Events:", this.events);
          }
        })
        .catch((error) => {
          console.error("Error fetching events:", error.response.data);
        });
    },
    fetchRegisteredEvents() {
      axios
        .get("/api/posts/events/register/")
        .then((response) => {
          // Assuming response.data contains an array of registered events
          this.registeredEvents = response.data;
          console.log(response.data); // Update the data property
        })
        .catch((error) => {
          // Log the error response for debugging
          console.error(
            "Error fetching registered events:",
            error.response ? error.response.data : error.message
          );

          // Optionally, you can show an error message in your UI
          this.errorMessage =
            "Failed to fetch registered events. Please try again later.";
        });
    },

    // Fetch events created by the user
    //     getEvents() {
    //     axios.get(/api/posts/events/user_events/${this.$route.params.id}/)

    //         .then((response )=> {
    //             // Handle success
    //             this.events = response.data.events;
    //             this.user = response.data.user;
    //             console.log(response.data);
    //         })
    //         .catch(error => {
    //             console.error("Error fetching events:", error);
    //         });
    // },

    // async fetchUserEvents(userId) {
    //   try {
    //     const response = await this.$http.get(/api/events/user/${this.$route.params.id}/); // Adjust API URL as necessary
    //     this.events = response.data.events;
    //     this.user = response.data.user; // Assuming user details are also fetched
    //   } catch (error) {
    //     console.error("Error fetching events:", error);
    //   }
    // },

    // Fetch events registered by the user
    // fetchRegisteredEvents() {
    //   axios
    //     .get(/api/registered-events/${this.userStore.user.id}/) // Adjust the endpoint accordingly
    //     .then((response) => {
    //       this.registeredEvents = response.data; // Assuming the response is an array of registered events
    //     })
    //     .catch((error) => {
    //       console.error("Error fetching registered events:", error);
    //     });
    // },

    // Handle file change for post images
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },

    // Handle post submission
    submitForm() {
      let formData = new FormData();
      formData.append("image", this.$refs.file.files[0]);
      formData.append("body", this.body);
      formData.append("title", this.title);
      formData.append("description", this.description);
      formData.append("contact_information", this.contact_information);
      formData.append("price", this.price);
      formData.append("category", this.category);
      formData.append("breed", this.breed);
      formData.append("color", this.color);
      formData.append("age", this.age);
      formData.append("vaccinated", this.vaccinated);
      formData.append("gender", this.gender);
      formData.append("weight", this.weight);
      formData.append("microchipped", this.microchipped);
      formData.append("trained", this.trained);
      formData.append("health_certificate", this.health_certificate);

      axios
        .post("/api/posts/create/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          this.posts.unshift(response.data);
          this.resetFormFields();
          this.user.posts_count += 1;
        })
        .catch((error) => {
          console.error("Error creating post:", error);
        });
    },

    // Reset form fields after submission
    resetFormFields() {
      this.body = "";
      this.title = "";
      this.description = "";
      this.contact_information = "";
      this.price = "";
      this.category = "";
      this.breed = "";
      this.color = "";
      this.age = null;
      this.vaccinated = "";
      this.gender = "";
      this.weight = null;
      this.microchipped = "";
      this.trained = "";
      this.health_certificate = "";
      this.$refs.file.value = null;
      this.url = null;
    },

    // Handle post deletion
    deletePost(postId) {
      axios
        .delete(`/api/posts/${postId}/delete/`)
        .then(() => {
          this.getFeed();
          this.toastStore.showToast(5000, "The post was deleted", "bg-red-500");
        })
        .catch((error) => {
          console.error("Error deleting post:", error);
        });
    },

    // Redirect to edit post page
    editPost(postId) {
      this.$router.push(`/${postId}/edit/`).catch((err) => {
        console.error("Navigation error:", err);
      });
    },
    editEvent(eventId) {
      // Assuming you are using Vue Router for navigation
      this.$router
        .push({ name: "EditEvent", params: { id: eventId } })
        .catch((err) => {
          console.error("Navigation error:", err);
        });
    },
    async deleteEvent(eventId) {
      console.log("Attempting to delete event with ID:", eventId); // Log event ID
      if (confirm("Are you sure you want to delete this event?")) {
        try {
          const deleteUrl = `/api/posts/events/${eventId}/delete/`; // Ensure this URL is correct
          await axios.delete(deleteUrl);

          // Update the UI after successful deletion
          this.events = this.events.filter((event) => event.id !== eventId);

          alert("Event deleted successfully");
        } catch (error) {
          console.error(
            "Failed to delete event:",
            error.response ? error.response.data : error.message
          );
          alert("Error deleting event. Please try again.");
        }
      }
    },

    // Logout function
    logout() {
      this.userStore.removeToken();
      this.$router.push("/login");
    },
  },
};
</script>
