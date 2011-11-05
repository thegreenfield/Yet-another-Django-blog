from django.conf.urls.defaults import patterns


urlpatterns = patterns('blog.views',
   (r"^post/(\d+)(/.*)?$", "post"),
   (r"^add_comment/(\d+)/$", "add_comment"),
   (r"^delete_comment/(\d+)/$", "delete_comment"),
   (r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
   (r"", "main"),
)
