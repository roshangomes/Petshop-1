import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import FeedView from "../views/FeedView.vue";
import SignupView from "../views/SignupView.vue";
import LoginView from "../views/LoginView.vue";
import SearchView from "../views/SearchView.vue";
import ProfileView from "../views/ProfileView.vue";
import FriendsView from "../views/FriendsView.vue";
import PostView from "../views/PostView.vue";
import ChatView from "../views/ChatView.vue";
import TrendView from "../views/TrendView.vue";
import EditProfileView from "../views/EditProfileView.vue";
import EditPasswordView from "../views/EditPasswordView.vue";
import NotificationsView from "../views/NotificationsView.vue";
import EventList from "../views/EventList.vue";
import EventForm from "../views/EventForm.vue";
import Bookmarked from "../views/Bookmarked.vue";
import FeedForm from "../views/FeedForm.vue";
import PostEdit from "../views/PostEdit.vue";
import EventHome from "../views/EventHome.vue";
import Hero from "../components/Hero.vue";
import EventDetails from "../views/EventDetails.vue";
import EventRegister from "../views/EventRegister.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/feed",
      name: "feed",
      component: FeedView,
    },
    {
      path: "/feedform",
      name: "FeedForm",
      component: FeedForm,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/search",
      name: "search",
      component: SearchView,
    },
    {
      path: "/chat",
      name: "chat",
      component: ChatView,
    },
    {
      path: "/notifications",
      name: "notifications",
      component: NotificationsView,
    },
    {
      path: "/profile/edit",
      name: "editprofile",
      component: EditProfileView,
    },
    {
      path: "/profile/edit/password",
      name: "editpassword",
      component: EditPasswordView,
    },
    {
      path: "/profile/:id",
      name: "profile",
      component: ProfileView,
    },
    {
      path: "/profile/:id/friends",
      name: "friends",
      component: FriendsView,
    },
    {
      path: "/:id",
      name: "postview",
      component: PostView,
    },
    {
      path: "/:id/edit",
      name: "postedit",
      component: PostEdit,
    },

    {
      path: "/events",
      name: "EventList",
      component: EventList,
    },
    {
      path: "/events/create",
      name: "EventForm",
      component: EventForm,
    },

    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/bookmarks",
      name: "bookmarked-posts",
      component: Bookmarked,
    },
    {
      path: "/",
      component: Hero,
    },

    {
      path: "/pet-events",
      component: EventHome,
    },
    {
      path: "/event/:id", // Dynamic route for event details
      name: "EventDetails",
      component: EventDetails,
    },
    {
      path: "/event/:id",
      name: "eventregister",
      component: EventRegister,
    },
  ],
});

export default router;
