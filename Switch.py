class Switch:
	CATEGORY = "Switch"
	FUNCTION = "run"
	RETURN_TYPES = ("*",)
 
	def __init__(self):
		pass

	@classmethod
	def INPUT_TYPES(self):
		return {
			"required": {
				"Switch": ("BOOLEAN", { "default": True, "label_on": "case1", "label_off": "case2" }),
			},
			"optional": {
				"case1": ("*",),
    		"case2": ("*",)
			}
		}

	def run(self, Switch, case1, case2):
		return ((case1 if Switch else case2),)

NODE_CLASS_MAPPINGS = {
	"Switch": Switch
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"Switch": "Switch",
}
