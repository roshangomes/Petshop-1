<template>
  <div>
    <header class="bg-blue-50 p-4 flex justify-between items-center">
      <div class="flex space-x-4">
        <input
          type="text"
          placeholder="Search"
          class="border border-gray-300 p-2 rounded-md"
        />
        <input
          type="text"
          placeholder="Category"
          class="border border-gray-300 p-2 rounded-md"
        />
        <input
          type="text"
          placeholder="Location"
          class="border border-gray-300 p-2 rounded-md"
        />
      </div>
    </header>

    <section class="bg-gray-100 py-8">
      <h1 class="text-center text-3xl font-bold mb-4">
        Upcoming Pet Events in India
      </h1>
      <div class="flex justify-center space-x-4">
        <div class="bg-orange-200 p-4 rounded-lg">
          <h2 class="text-lg font-bold">Pet Event</h2>
          <p class="text-sm">Location: Parade Ground, Chandigarh</p>
          <p class="text-sm">Date: 21st - 22nd December 2024</p>
        </div>
        <div class="bg-green-200 p-4 rounded-lg">
          <h2 class="text-lg font-bold">India International Pet Trade Fair</h2>
          <p class="text-sm">Location: Bombay Exhibition Centre, Mumbai</p>
          <p class="text-sm">Date: 5th & 6th October 2024</p>
        </div>
        <div class="bg-blue-200 p-4 rounded-lg">
          <h2 class="text-lg font-bold">Petop Gala</h2>
          <p class="text-sm">Location: Sakal Media Group</p>
        </div>
      </div>
    </section>

    <section class="bg-white py-8">
      <div class="flex justify-between items-center px-8">
        <h2 class="text-xl font-bold">Upcoming Events this Month</h2>
        <button class="text-blue-500">View All →</button>
      </div>
    </section>

    <div v-if="events.length">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
        <div
          v-for="event in events"
          :key="event.id"
          @click="goToEventDetails(event.id)"
          class="border border-gray-200 p-4 rounded-lg shadow-sm bg-white flex flex-col justify-between"
        >
          <div>
            <div v-if="event.attachments.length">
              <div
                v-for="attachment in event.attachments"
                :key="attachment.id"
                class="mb-6"
              >
                <img
                  :src="attachment.image_url"
                  alt="Event Image"
                  class="w-full h-48 object-cover rounded"
                />
              </div>
            </div>
            <h2 class="text-xl font-semibold mb-2">{{ event.title }}</h2>
            <p class="text-gray-700 mb-2">{{ event.description }}</p>
            <p class="text-gray-500 mb-2">{{ event.date }}</p>
            <p class="text-gray-500 mb-4">{{ event.location }}</p>
          </div>

          <router-link
            :to="{ name: 'EventDetails', params: { id: event.id } }"
            class="mt-auto"
          >
            <button
              class="bg-blue-500 text-white font-bold py-2 px-4 rounded-lg w-full"
            >
              View Event
            </button>
          </router-link>
        </div>
      </div>
    </div>
    <div v-else>
      <p class="text-gray-700">No events available.</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { RouterLink } from "vue-router";
export default {
  name: "EventHome",

  data() {
    return {
      events: [],
    };
  },
  created() {
    this.fetchEvents();
  },
  methods: {
    fetchEvents() {
      axios
        .get("/api/posts/events/")
        .then((response) => {
          this.events = response.data;
        })
        .catch((error) => {
          console.error("Error fetching events:", error.response.data);
        });
    },
  },
  goToEventDetails(eventId) {
    this.$router.push(`/event/${eventId}`);
  },
};
</script>

<style scoped>
header {
  border-bottom: 1px solid #e5e5e5;
}
section {
  margin-top: 20px;
}
</style>

<!-- <template>
  <div class="bg-orange-100">
    <Adoption />

    <header class="p-4">
      <div class="space-x-4 flex justify-center">
        <select
          v-model="selectedCategory"
          @change="filterEvents"
          class="border border-gray-300 p-2 rounded-md"
        >
          <option value="">All Categories</option>
          <option value="Workshop">Workshop</option>
          <option value="Seminar">Seminar</option>
          <option value="Networking">Networking</option>
          <option value="Exhibition">Exhibition</option>
          <option value="Webinar">Webinar</option>
          <option value="Conference">Conference</option>
          <option value="Meetup">Meetup</option>
          <option value="Uncategorized">Uncategorized</option>
        </select>

        <select
          v-model="selectedLocation"
          @change="filterEvents"
          class="border border-gray-300 p-2 rounded-md"
        >
          <option value="">All Locations</option>
          <option value="Delhi">Delhi</option>
          <option value="Mumbai">Mumbai</option>
          <option value="Bengaluru">Bengaluru</option>
          <option value="Chennai">Chennai</option>
          <option value="Kolkata">Kolkata</option>
          <option value="Hyderabad">Hyderabad</option>
          <option value="Ahmedabad">Ahmedabad</option>
          <option value="Pune">Pune</option>
          <option value="Jaipur">Jaipur</option>
        </select>

        <div class="flex space-x-2">
          <input
            type="number"
            v-model="minPrice"
            @change="filterEvents"
            placeholder="Min Price"
            class="border border-gray-300 p-2 rounded-md"
          />
          <input
            type="number"
            v-model="maxPrice"
            @change="filterEvents"
            placeholder="Max Price"
            class="border border-gray-300 p-2 rounded-md"
          />
        </div>
      </div>
    </header>
    <section class="py-8">
      <h1 class="text-center text-3xl font-bold mb-4">
        Upcoming Pet Events in India
      </h1>
      <div class="flex justify-center space-x-4 flex-wrap">
        <div
          v-for="event in filteredEvents"
          :key="event.id"
          class="border border-gray-200 p-4 rounded-lg shadow-sm bg-white w-72 h-96 flex flex-col justify-between"
        >
          <div>
            <h2 class="text-xl font-semibold mb-2">{{ event.title }}</h2>
            <div v-if="event.attachments && event.attachments.length">
              <div
                v-for="attachment in event.attachments"
                :key="attachment.id"
                class="mb-4"
              >
                <img
                  :src="attachment.image_url"
                  alt="Event Image"
                  class="w-full h-32 object-cover rounded"
                />
              </div>
            </div>
            <p class="text-gray-700 mb-2 line-clamp-3">
              {{ event.description }}
            </p>
          </div>
          <div>
            <p class="text-gray-500 mb-2">{{ event.date }}</p>
            <p class="text-gray-500 mb-2">Category: {{ event.category }}</p>
            <p class="text-gray-500 mb-4">Price: ₹{{ event.price }}</p>
            <p class="text-gray-500 mb-4">{{ event.location }}</p>
            <router-link
              :to="{ name: 'EventDetails', params: { id: event.id } }"
              class="mt-auto"
            >
              <button
                class="bg-blue-500 text-white font-bold py-2 px-4 rounded-lg w-full"
              >
                View Event
              </button>
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import Adoption from "../components/Adoption.vue";

export default {
  name: "EventHome",
  components: { Adoption },
  data() {
    return {
      events: [],
      filteredEvents: [],
      selectedCategory: "",
      selectedLocation: "",
      minPrice: null,
      maxPrice: null,
    };
  },
  created() {
    this.fetchEvents();
  },
  methods: {
    fetchEvents() {
      axios
        .get("/api/posts/events/")
        .then((response) => {
          this.events = response.data;
          this.filteredEvents = response.data;
        })
        .catch((error) => {
          console.error(
            "Error fetching events:",
            error.response ? error.response.data : error
          );
          alert("Failed to load events.");
        });
    },
    filterEvents() {
      this.filteredEvents = this.events.filter((event) => {
        const categoryMatch = this.selectedCategory
          ? event.category === this.selectedCategory
          : true;
        const locationMatch = this.selectedLocation
          ? event.location === this.selectedLocation
          : true;
        const priceMatch =
          (this.minPrice !== null ? event.price >= this.minPrice : true) &&
          (this.maxPrice !== null ? event.price <= this.maxPrice : true);
        return categoryMatch && locationMatch && priceMatch;
      });
    },
    bookmarkEvent(eventId) {
      axios
        .post("/api/bookmarks/", { event: eventId })
        .then(() => {
          alert("Event bookmarked successfully!");
        })
        .catch((error) => {
          console.error(
            "Error bookmarking event:",
            error.response ? error.response.data : error
          );
          alert("Failed to bookmark the event.");
        });
    },
  },
};
</script>

<style scoped>
header {
  border-bottom: 1px solid #e5e5e5;
}
section {
  margin-top: 20px;
}
</style> -->
