#include <gtk/gtk.h>
#include <stdlib.h>

static void end(GtkWidget *widget, gpointer data)
{
    exit(-1);
}

static void activate(GtkApplication *app, gpointer user_data)
{
    GtkWidget *window;
    GtkWidget *frame;
    GtkWidget *grid;
    GtkWidget *infolabel;
    GtkWidget *logo;
    GdkPixbuf *pb;
    GtkWidget *label2;
    GtkWidget *exit_button;
    const char *text = "Website";
    const char *format = "<a href ='https://linux.tcetmumbai.in//' title='Check out our website!'><b>%s</b></a>";
    char *markup;

    const char *info = "TCET - Linux \n\n1.0\n\nTCET Linux is GNU/Linux distribution, based on Arch Linux built for enhancing college infrastructure and promoting Linux in software engineering education\n\n\n ©2020-2024 TCET-Opensource";

    window = gtk_application_window_new(app);

    gtk_window_set_title(GTK_WINDOW(window), "Window");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 100);
    gtk_window_set_resizable(GTK_WINDOW(window), FALSE);

    frame = gtk_frame_new("");
    gtk_widget_set_margin_top(frame, 5);
    gtk_widget_set_margin_start(frame, 5);
    gtk_widget_set_margin_bottom(frame, 5);
    gtk_widget_set_margin_end(frame, 5);

    grid = gtk_grid_new();
    gtk_grid_set_column_spacing(GTK_GRID(grid), 10);
    gtk_grid_set_row_spacing(GTK_GRID(grid), 10);
    gtk_grid_set_column_homogeneous(GTK_GRID(grid), FALSE);

    infolabel = gtk_label_new(info);
    gtk_label_set_line_wrap(GTK_LABEL(infolabel), TRUE);
    gtk_label_set_justify(GTK_LABEL(infolabel), GTK_JUSTIFY_CENTER);
    gtk_label_set_max_width_chars(GTK_LABEL(infolabel), 50);
    gtk_widget_set_margin_start(infolabel, 10);
    gtk_widget_set_margin_end(infolabel, 10);
    gtk_widget_set_hexpand(infolabel, TRUE);

    logo = gtk_image_new();
    gtk_image_set_pixel_size(GTK_IMAGE(logo), 150);
    gtk_image_set_from_file(GTK_IMAGE(logo), "./a.png");
    label2 = gtk_label_new(NULL);

    markup = g_markup_printf_escaped(format, text);
    gtk_label_set_markup(GTK_LABEL(label2), markup);
    g_free(markup);
    gtk_label_set_line_wrap(GTK_LABEL(label2), TRUE);
    gtk_label_set_max_width_chars(GTK_LABEL(label2), 48);
    gtk_label_set_justify(GTK_LABEL(label2), GTK_JUSTIFY_CENTER);

    exit_button = gtk_button_new_with_label("Back");
    g_signal_connect(exit_button, "clicked", G_CALLBACK(end), NULL);
    gtk_grid_attach(GTK_GRID(grid), exit_button, 2, 10, 2, 1);
    gtk_grid_attach(GTK_GRID(grid), infolabel, 0, 2, 4, 2);
    gtk_grid_attach(GTK_GRID(grid), label2, 0, 3, 5, 2);
    gtk_grid_attach(GTK_GRID(grid), logo, 0, 0, 4, 1);


    gtk_container_add(GTK_CONTAINER(frame), grid);

    gtk_container_add(GTK_CONTAINER(window), frame);
    
    gtk_widget_show_all(window);
}

int main(int argc, char **argv)
{
    GtkApplication *app;
    int status;

    app = gtk_application_new("org.gtk.example", G_APPLICATION_FLAGS_NONE);
    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);
    status = g_application_run(G_APPLICATION(app), argc, argv);
    g_object_unref(app);

    return status;
}
