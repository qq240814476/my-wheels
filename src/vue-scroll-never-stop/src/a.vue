<template>
  <div>
    <div class="container" ref="observe-root">
      <section class="list-item" v-for="item in items" :key="item.id">{{item.name}}</section>
    </div>
    <Observer @intersect="intersected" :options="options"/>
  </div>
</template>

<script>
import Observer from "./b";

export default {
  data: () => ({ page: 1, items: [], options: null }),
  methods: {
    async intersected() {
      const res = await fetch(`https://jsonplaceholder.typicode.com/comments?_page=${
        this.page
      }&_limit=20`);

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

<style lang="less">
.container{
  height: 400px;
  width: 300px;
  overflow: auto;
   .list-item{
    height: 40px;
    border: 1px solid #eee;
    border-radius: 3px;
    background: #777777;
  }
}
</style>