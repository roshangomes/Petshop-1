<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-3 space-y-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-if="post.id"
      >
        <FeedDetail v-bind:post="post" />
      </div>

      <div
        class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"
        v-for="comment in post.comments"
        v-bind:key="comment.id"
      >
        <CommentItem v-bind:comment="comment" />
      </div>

      <div class="bg-white border border-gray-200 rounded-lg">
        <form v-on:submit.prevent="submitForm" method="post">
          <div class="p-4">
            <textarea
              v-model="body"
              class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="What do you think?"
            ></textarea>
          </div>

          <div class="p-4 border-t border-gray-100">
            <button
              class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
            >
              Comment
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import CommentItem from "../components/CommentItem.vue";
import FeedDetail from "../components/FeedDetail.vue";

export default {
  name: "PostView",

  components: {
    // FeedItem,
    CommentItem,
    FeedDetail,
  },

  data() {
    return {
      post: {
        id: null,
        comments: [],
      },
      body: "",
    };
  },

  mounted() {
    this.getPost();
  },

  methods: {
    getPost() {
      axios
        .get(`/api/posts/${this.$route.params.id}/`)
        .then((response) => {
          this.post = response.data.post;
        })
        .catch((error) => {
          console.error(
            "Error fetching post:",
            error.response ? error.response.data : error.message
          );
        });
    },

    submitForm() {
      axios
        .post(`/api/posts/${this.$route.params.id}/comment/`, {
          body: this.body,
        })
        .then((response) => {
          this.post.comments.push(response.data);
          this.body = "";
        })
        .catch((error) => {
          console.error(
            "Error submitting comment:",
            error.response ? error.response.data : error.message
          );
        });
    },
  },
};
</script>
