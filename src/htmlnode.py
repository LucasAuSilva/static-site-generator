
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""

        props_text = " ".join(
            map(
                lambda x: f"{x[0]}=\"{x[1]}\"",
                self.props.items()
            ))

        print(props_text)
        return props_text

    def __repr__(self):
        return f"<{self.tag}> {self.value} </{self.tag}>\nprops: {self.props}\nchildren: {self.children}"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

