from django.contrib import admin
from .models import Genre, Book, Order
# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'book_count']
    search_fields = ['name', 'description']
    prepopulated_fields = { 'slug' : ('name',)}
    
    def book_count(self, obj):
        return obj.book_set.count()
    
    book_count.short_description = "Number of Books"






@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'added_by', 'price_cents', 'page_count', 'status', 'published_date']
    list_filter = ['status', 'genre', 'published_date']
    search_fields = ['title', 'added_by__username']
    readonly_fields = ['published_date']
    raw_id_fields = ['added_by']
    ordering = ['-published_date']
    
    fieldsets = (
        ("Book Information", {
            'fields' : ('title', 'genre', 'added_by')
        }),
        ("Pricing & Status", {
            'fields' : ('price_cents', 'page_count', 'status')
        }),
        ("Metadata", {
            'classes' : ('collapse',),
            'fields' : ['published_date']
        })
    ) 






@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'total_amount', 'is_paid', 'timestamp']
    list_filter = ['is_paid', 'timestamp']
    search_fields = ['book__title']
    readonly_fields = ['timestamp']
    raw_id_fields = ['book']
    date_hierarchy = 'timestamp'
