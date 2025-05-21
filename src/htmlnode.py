
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
