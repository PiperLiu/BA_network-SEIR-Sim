import G6 from '@antv/g6'
import { data } from '@/hooks/dataHook'

const g6init = () => {
  const graph = new G6.Graph({
    container: 'mountNode'
  })

  graph.data(data) // 读取 Step 2 中的数据源到图上
  graph.render() // 渲染图
}

export {
  g6init
}
