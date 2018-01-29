#coding:utf-8

class Page_set(object):
    """
    current_page:当前页码
    total_data:数据总量
    access_url:页码加载的接口
    per_page_item_num:每页显示的数量，前端可选择
    display_page_num:前端显示可随意点击的页码个数
    """
    def __init__(self,total_data,access_url,current_page=1,per_page_item_num=5,display_page_num=5):
        self.current_page = int(current_page)
        print self.current_page
        print type(self.current_page)
        self.tatal_data = int(total_data)
        self.per_page_item_num = int(per_page_item_num)
        self.display_page_num = int(display_page_num)
        self.access_url = access_url

    # 每页数据选值的初始索引
    @property
    def start_index(self):
        result = (self.current_page - 1) * self.per_page_item_num
        return result

    # 每页数据选值的结束索引
    @property
    def end_index(self):
        result = self.current_page * self.per_page_item_num
        return result

    # 数据的总页数，方便前端查看还剩多少页到最后
    @property
    def total_page_num(self):
        temp = divmod(self.tatal_data,self.per_page_item_num)
        if temp[1]:
            total_page_num = temp[0]+1
        else:
            total_page_num = temp[0]
        return  total_page_num

    #展示在前端显示多少个页面可点击，比如1.2.3.4.5
    @property
    def display_page(self):
        # 判断总页数与展示的页数
        if self.total_page_num <= self.display_page_num:
            return range(1,self.total_page_num+1)
        else:
            # 当前页码小于展示页的一半加一时，前端就显示固定展示页面即可
            if self.current_page <= self.display_page_num / 2 + 1:
                return range(1,self.display_page_num+1)
            else:
                # 当前页码加上展示页的一半+1大于总页数时，从总页数往前倒推展示页码数
                if self.current_page+ self.display_page_num / 2 + 1 >= self.total_page_num:
                    return range(self.total_page_num-self.display_page_num,self.total_page_num+1)
                else:
                    # 如果以上的情况都不属于，直接显示当前页加展示页的前后一半
                    return range(self.current_page-self.display_page_num/2,self.current_page+self.display_page_num/2+1)

    #基本页码渲染到前端，比如首页上一页以及中间显示多少几个页码等
    @property
    def page_render(self):
        """
        per_page_item_num:每个页面显示的数量，供前端选择
        first_page:第一个页面
        prev_page:前一页
        temp:固定展示的页面个数
        next_page:下一页
        last_page:直接跳转到最后一页
        current_total_page:当数据量庞大的时候，方便当前页距离总的还有多少
        :return:
        """
        page_list = []
        per_page_item_num = '<li><a>每页:<select> \
                <option value="6">6</option> \
                <option value="10">10</option> \
                <option value="20">20</option> \
            </select></a></li>'
        first_page = '<li><a href="{}{}">首页</a></li>'.format(self.access_url,1)
        if self.current_page <= 1:
            prev_page = '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">上一页</span></a></li>'
        else:
            prev_page = '<li><a href="{}{}" aria-label="Previous"><span aria-hidden="true">上一页</span></a></li>'.format(self.access_url,self.current_page-1)
        list(page_list.append(i) for i in [per_page_item_num,first_page,prev_page])
        for i in self.display_page:
            if i == self.current_page:
                temp = '<li class="active"><a href="{}{}">{}<span class="sr-only">(current)</span></a></li>'.format(self.access_url,i,i)
            else:
                temp = '<li><a href="{}{}">{}</a></li>'.format(self.access_url,i,i)
            page_list.append(temp)
        if self.current_page >= self.total_page_num:
            next_page = '<li class="disabled"><a href="#" aria-label="Next"><span aria-hidden="true">下一页</span></a></li>'
        else:
            next_page = '<li><a href="{}{}" aria-label="Next"><span aria-hidden="true">下一页</span></a></li>'.format(self.access_url,self.current_page+1)
        if self.total_page_num == 0:
            last_page = '<li><a href="{}{}">尾页</a></li>'.format(self.access_url,1)
        else:
            last_page = '<li><a href="{}{}">尾页</a></li>'.format(self.access_url, self.total_page_num)
        current_total_page = '<li><a>第{}页/共{}页</a></li>'.format(self.current_page,self.total_page_num)
        list(page_list.append(i) for i in [next_page,last_page,current_total_page])
        return ''.join(page_list)




