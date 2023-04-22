import glfw
from TP.vulkan.vulkan import *

glfw.init()
glfw.window_hint(glfw.CLIENT_API, glfw.NO_API)
window = glfw.create_window(
    width=800, height=600, title="test_vulkan", monitor=None, share=None
)

print(glfw.vulkan_supported())
c = vkEnumerateInstanceExtensionProperties(None)
c = [e.extensionName for e in c]
print(len(c), "supported", c)
