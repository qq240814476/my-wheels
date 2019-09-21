<template>
  <div>
    <ul>
      <li class="list-item" v-for="item in items" :key="item.id">{{item.name}}</li>
    </ul>
    <Observer @intersect="intersected"/>
  </div>
</template>

<script>
import Observer from "./b";

export default {
  data: () => ({ page: 1, items: [] }),
  methods: {
    async intersected() {
      const res = await fetch(`https://jsonplaceholder.typicode.com/comments?_page=${
        this.page
      }&_limit=50`);

      this.page++;
      const items = await res.json();
      this.items = [...this.items, ...items];
    },
  },
  components: {
    Observer,
  },
};
</script>