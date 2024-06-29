import streamlit as st
from supabase_helpers import list_posts, user_likes_post, user_unlikes_post, check_if_user_likes_post
from constants import IDEAS_TABLE, USERS_TABLE


def like_post(i, post):
    user_likes_post(st.session_state.user_id, post["id"])
    st.session_state.posts[i]["like_count"] += 1
    st.session_state.posts[i]["has_liked"] = True

def unlike_post(i, post):
    user_unlikes_post(st.session_state.user_id, post["id"])
    st.session_state.posts[i]["like_count"] -= 1
    st.session_state.posts[i]["has_liked"] = False

def feed_page():
    st.session_state.posts = list_posts()
    for post in st.session_state.posts:
        post["has_liked"] = check_if_user_likes_post(st.session_state.user_id, post["id"])

    for i, post in enumerate(st.session_state.posts):
        idea = post[IDEAS_TABLE]
        user = post[USERS_TABLE]
        st.markdown(f"#### {idea["summary"]}")
        st.markdown(f"*{idea["description"]}*")
        st.markdown(f"*Created: {idea["created_at"]}*")
        st.write(f"Idea by **{user["first_name"]} {user["last_name"]}** ({user["email"]})")
        if post["has_liked"]:
            st.button(f":heart: {post["like_count"]}", key=f"unlike_{i}", type="primary", on_click=unlike_post, args=(i, post))
        else:
            st.button(f":heart: {post["like_count"]}", key=f"like_{i}", on_click=like_post, args=(i, post))
        st.divider()
    
