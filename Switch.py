# 와일드 카드를 속이는 용도? 임팩트팩에서 가져옴
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_typ = AnyType("*")

class NodeSwitch:
	def __init__(self):
		pass

	@classmethod
	def INPUT_TYPES(self):
		return {
			"required": {
				"DeTK": ("BOOLEAN", { "default": True, "label_on": "case1", "label_off": "case2" }),
			},
			"optional": {
				"case1": (any_typ,),
    		"case2": (any_typ,)
			}
		}
	CATEGORY = "Switch"
	FUNCTION = "run"
	RETURN_TYPES = (any_typ,)

	def run(self, DeTK, case1, case2):
		return ((case1 if DeTK else case2),)

NODE_CLASS_MAPPINGS = {
	"NodeSwitch": NodeSwitch
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"NodeSwitch": "NodeSwitch",
}
