<script setup lang="ts">
import { g6init } from '@/hooks/g6Hook'
import { onMounted } from 'vue'
onMounted(() => {
  g6init()
})
</script>

<template>
  <template id="container">
    <div class="node__wrapper" id="mountNode"></div>
    <div id="operatorPanel"></div>
  </template>
</template>

<style>
#container {
  text-align: center;
  display: flex;
  width: 100vw;
  justify-content: center;
  align-items: center;
}

.node__wrapper {
  width: 75vh;
  height: 75vh;
  border-radius: 24px;
  background: #ede8e8;
  box-shadow:  12px 12px 23px #bbb7b7,
              -12px -12px 23px #ffffff;
}

#operatorPanel {
  width: 30vh;
  height: 30vh;
  border-radius: 24px;
  margin: 20px;
  background: #ede8e8;
  box-shadow: inset 12px 12px 23px #bbb7b7,
              inset -12px -12px 23px #ffffff;
}
</style>
